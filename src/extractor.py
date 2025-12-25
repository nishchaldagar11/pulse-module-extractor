from collections import defaultdict


class ModuleExtractor:
    def __init__(self):
        pass

    def extract_modules(self, sections):
        """
        Convert parsed sections into Modules & Submodules
        Logic:
        - H1 / H2 -> Modules
        - H3      -> Submodules
        """
        modules = defaultdict(lambda: {
            "description": "",
            "submodules": defaultdict(str)
        })

        current_module = None

        for section in sections:
            title = section["title"]
            level = section["level"]
            content_text = " ".join(section["content"])

            if level in ["h1", "h2"]:
                current_module = title
                if not modules[current_module]["description"]:
                    modules[current_module]["description"] = content_text[:300]

            elif level == "h3" and current_module:
                if not modules[current_module]["submodules"][title]:
                    modules[current_module]["submodules"][title] = content_text[:300]

        return modules

    def format_output(self, modules):
        """
        Convert internal dict to final JSON format
        """
        output = []

        for module, data in modules.items():
            output.append({
                "module": module,
                "description": data["description"],
                "submodules": dict(data["submodules"])
            })

        return output
