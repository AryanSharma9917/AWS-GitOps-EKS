package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	tenantName := "tenant1"
	image := "nginx:latest"
	tier := "basic" // Change this as needed

	// Read tenant template
	template, err := os.ReadFile("tenants/tenant-template.yaml")
	if err != nil {
		panic(err)
	}

	// Replace placeholders in the template
	output := strings.ReplaceAll(string(template), "{{ .tenantName }}", tenantName)
	output = strings.ReplaceAll(output, "{{ .image }}", image)

	// Read tier-specific values and append
	tierPath := fmt.Sprintf("tenants/tiers/%s-values.yaml", tier)
	tierData, err := os.ReadFile(tierPath)
	if err != nil {
		panic(err)
	}
	output += "\n" + string(tierData)

	// Write final config to output path
	outPath := fmt.Sprintf("flux/tenants/tenant-%s.yaml", tenantName)
	err = os.WriteFile(outPath, []byte(output), 0644)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Tenant config written to %s\n", outPath)
}
