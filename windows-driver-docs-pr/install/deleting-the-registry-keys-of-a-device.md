---
title: Delete the registry keys of a device
description: Provides information about how to delete the registry keys of a device.
keywords:
- registry WDK device installations, delete a device's registry keys
- delete registry keys WDK device installations
ms.date: 08/29/2022
---

# Delete the registry keys of a device

You should not use [**CM_Delete_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_delete_devnode_key) or [**SetupDiDeleteDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey) to delete the *software keys* or *hardware keys* for the device for the following reasons:

- [**CM_Delete_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_delete_devnode_key) and [**SetupDiDeleteDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey) remove all custom settings in registry keys. This includes the following:

  - Settings that were specified during installation.

  - Settings that were created or modified by the device driver.

  - Settings that were created or modified by applications or other components.

    [**CM_Delete_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_delete_devnode_key) and [**SetupDiDeleteDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey) also remove critical device installation state.

- Software or hardware keys that are opened by using [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) with a scope of DICS_FLAG_GLOBAL contain data about the device installation state. Software or hardware keys that are accessed with a scope of DICS_FLAG_CONFIGSPECIFIC do not contain device installation state.

    In either case, deleting these software or hardware keys could have implications for other device installation components.

You should not make assumptions about whether device registry keys are present. When the device is uninstalled, the system automatically deletes all software and hardware keys for the device.

You can safely create and delete registry subkeys under the hardware or software keys by using standard registry functions. By using these functions, you avoid naming collisions between the system and other components. Also, if you create subkeys by using these functions, the subkey inherits the default permissions of the parent registry key. For more information, see [Opening, creating, and closing keys](/windows/win32/sysinfo/opening-creating-and-closing-keys).

For more information about the standard registry functions, see [Registry functions](/windows/win32/sysinfo/registry-functions).
