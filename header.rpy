init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Otter compliments",
        description="New 'I want to tell you something' options.",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Otter compliments",
            user_name="my-otter-self",
            repository_name="otter_MAS_compliments"
        )
