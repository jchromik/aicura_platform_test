import cbdf_api

def test_components():
    template = cbdf_api.generate_templates.gather_cbdf_api_objects("aicura_platform_tutorial")
    components = set()
    for _, value in template.items():
        for j in ["architectures", "initializers", "preprocessors", "augmentations", "metrics", "losses", "optimizers", "callbacks", "preprocessors", "postprocessors"]:
            c = value.get(j)
            if c is not None and list(c) != []:
                components.update(c)
    print("Discovered components:")
    for i in sorted(components):
        print(f"\t{i}")
    assert len(components) > 0