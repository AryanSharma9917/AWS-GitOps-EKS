import os
import yaml

TEMPLATE_PATH = "tenants/tenant-template.yaml"
NAMESPACE_TEMPLATE_PATH = "tenants/namespace-template.yaml"
OUTPUT_TENANT_PATH = "flux/tenants/tenant-{name}.yaml"
OUTPUT_NAMESPACE_PATH = "flux/tenants/namespace-{name}.yaml"

def onboard_tenant(name, tier="standard"):
    # Read and process tenant template
    with open(TEMPLATE_PATH, 'r') as f:
        template = f.read()
    
    tier_file = f"tenants/tiers/{tier}-values.yaml"
    with open(tier_file, 'r') as f:
        tier_values = f.read()

    processed = template.replace("{{ .tenantName }}", name).replace("{{ .image }}", "nginx:latest")
    processed += "\n" + tier_values

    os.makedirs("flux/tenants", exist_ok=True)

    with open(OUTPUT_TENANT_PATH.format(name=name), 'w') as f:
        f.write(processed)

    # Read and process namespace template
    with open(NAMESPACE_TEMPLATE_PATH, 'r') as f:
        namespace_template = f.read()
    namespace_yaml = namespace_template.replace("{{ .tenantName }}", name)

    with open(OUTPUT_NAMESPACE_PATH.format(name=name), 'w') as f:
        f.write(namespace_yaml)

    print(f"Tenant '{name}' with tier '{tier}' and namespace created.")
