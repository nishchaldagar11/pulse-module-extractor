def clean_text(text):
    """
    Basic cleanup for extracted content
    """
    if not text:
        return ""
    text = text.replace("\n", " ").strip()
    return " ".join(text.split())


def generate_summary(text, max_length=250):
    """
    Rule-based summarization:
    - Clean text
    - Trim to max length
    - Deterministic & explainable
    """
    text = clean_text(text)

    if len(text) <= max_length:
        return text

    return text[:max_length].rsplit(" ", 1)[0] + "..."


class DescriptionSummarizer:
    def __init__(self, max_length=250):
        self.max_length = max_length

    def summarize_modules(self, modules):
        """
        Generate summaries for modules and submodules
        """
        summarized_output = []

        for module in modules:
            module_desc = generate_summary(
                module.get("description", ""),
                self.max_length
            )

            submodules_summary = {}
            for sub_name, sub_desc in module.get("submodules", {}).items():
                submodules_summary[sub_name] = generate_summary(
                    sub_desc,
                    self.max_length
                )

            summarized_output.append({
                "module": module.get("module"),
                "description": module_desc,
                "submodules": submodules_summary
            })

        return summarized_output
