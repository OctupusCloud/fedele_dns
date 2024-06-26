from extras.plugins import PluginMenuButton, PluginMenuItem
from extras.plugins import PluginMenu
from utilities.choices import ButtonColorChoices

view_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:view_list",
    link_text="Views",
    permissions=["fedele_dns.view_view"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:view_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_view"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:view_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_view"],
        ),
    ),
)

zone_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:zone_list",
    link_text="Zones",
    permissions=["fedele_dns.view_zone"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:zone_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_zone"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:zone_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_zone"],
        ),
    ),
)

nameserver_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:nameserver_list",
    link_text="Nameservers",
    permissions=["fedele_dns.view_nameserver"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:nameserver_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_nameserver"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:nameserver_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_nameserver"],
        ),
    ),
)

record_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:record_list",
    link_text="Records",
    permissions=["fedele_dns.view_record"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:record_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_record"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:record_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_record"],
        ),
    ),
)

managed_record_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:managed_record_list",
    link_text="Managed Records",
    permissions=["fedele_dns.view_record"],
)

registrar_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:registrar_list",
    link_text="Registrars",
    permissions=["fedele_dns.view_registrar"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:registrar_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_registrar"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:registrar_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_registrar"],
        ),
    ),
)

contact_menu_item = PluginMenuItem(
    link="plugins:fedele_dns:contact_list",
    link_text="Contacts",
    permissions=["fedele_dns.view_contact"],
    buttons=(
        PluginMenuButton(
            "plugins:fedele_dns:contact_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["fedele_dns.add_contact"],
        ),
        PluginMenuButton(
            "plugins:fedele_dns:contact_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["fedele_dns.add_contact"],
        ),
    ),
)

menu_items = [view_menu_item, zone_menu_item, nameserver_menu_item, record_menu_item, managed_record_menu_item, registrar_menu_item, contact_menu_item]

# menu = PluginMenu(
#     label="NetBox DNS",
#     groups=(
#         (
#             "DNS Configuration",
#             (
#                 view_menu_item,
#                 zone_menu_item,
#                 nameserver_menu_item,
#                 record_menu_item,
#                 managed_record_menu_item,
#             ),
#         ),
#         (
#             "Domain Registration",
#             (
#                 registrar_menu_item,
#                 contact_menu_item,
#             ),
#         ),
#     ),
#     icon_class="mdi mdi-dns",
# )
