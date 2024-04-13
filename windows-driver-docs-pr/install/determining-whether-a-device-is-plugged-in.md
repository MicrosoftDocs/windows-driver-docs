---
title: Determining Whether a Device is Plugged in
description: Determining Whether a Device Is Plugged In
keywords:
- reinstalling unplugged devices
- unplugged device reinstallation WDK
- checking plugged in devices
- verifying plugged in devices
- plugged in device checks WDK
- determining plugged in devices WDK
ms.date: 04/20/2017
---

# Determining Whether a Device Is Plugged In


Be aware that the behavior of an AutoRun-invoked *device installation application* must depend on whether the user plugs in the hardware first or inserts the distribution medium first. Since independent hardware vendors (IHVs) typically provide one distribution disk, and a disk can only have one AutoRun-invoked application, your AutoRun-invoked device installation application must determine whether your device is plugged in.

To determine whether a device is plugged in, the application can call the [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa) function, passing the hardware ID of the device. The device is plugged in if one of the following is true:

-   The function returns **TRUE**. (This also installs the driver for the device.)

-   The function returns **FALSE** and the Win32 [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)function returns ERROR_NO_MORE_ITEMS. (No installation occurs.)

The device is not plugged in if the function returns **FALSE** and [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns NO_SUCH_DEVINST. (No installation occurs.)

### Reinstalling an Unplugged Device

When a device that formerly was attached is now unplugged, the device's *devnode* remains in the system, although it is both inactive and hidden. Before you can reinstall such a device, you must first find this "phantom" devnode, and mark it as needing reinstallation. Then, when the device is plugged back in, Plug and Play will reenumerate the device, find the new driver for it, and install the driver for the device.

**To reinstall an unplugged device:**

1.  Call the [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa) function.

    The [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa) function ensures that the correct INF file is present in the *%SystemRoot%\\inf* directory.

2.  Find the unplugged devices.

    Call the [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) function. In the call to this function, clear the DIGCF_PRESENT flag in the *Flags* parameter. You have to find *all* devices, not just those that are present. You can narrow the results of your search by specifying the particular device class in the *ClassGuid* parameter.

3.  Find the hardware IDs and compatible IDs of unplugged devices.

    **SetupDiGetClassDevs** returns a handle to the [device information set](device-information-sets.md) that contains all installed devices, whether plugged in or not, in the device class (assuming that you specified a device class in the first step). By making successive calls to the [**SetupDiEnumDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo) function, you can use this handle to enumerate all the devices in the device information set. Each call gives you an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure for the device. To obtain the list of hardware IDs, call the [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya) function with the *Property* parameter set to SPDRP_HARDWAREID. To obtain the list of the compatible IDs, call the same function, but with the *Property* parameter set to SPDRP_COMPATIBLEIDS. Both lists are MULTI-SZ strings.

4.  Look for a match between the ID of your device and the hardware IDs (or compatible IDs) of the previous step.

    Make sure that you perform full string comparisons between the hardware ID/compatible ID and the ID for your device. A partial comparison could lead to incorrect matches.

    When you find a match, call the [**CM_Get_DevNode_Status**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status) function, passing SP_DRVINFO_DATA.**DevInst** in the *dnDevInst* parameter. If this function returns CR_NO_SUCH_DEVINST, that confirms that the device is unattached (that is, has a phantom devnode).

5.  Mark the device.

    Call the [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya) function with the *Property* parameter set to SPDRP_CONFIGFLAGS. When this function returns, the *PropertyBuffer* parameter points to the device's **ConfigFlags** value from the registry. Perform a bitwise OR of this value with CONFIGFLAG_REINSTALL (defined in *Regstr.h*). After doing this, call the [**SetupDiSetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya) function, with the *Property* parameter set to SPDRP_CONFIGFLAGS, and the *PropertyBuffer* parameter set to the address of the device's modified **ConfigFlags** value This action modifies the registry's **ConfigFlags** value to incorporate the CONFIGFLAG_REINSTALL flag. This causes the device to be reinstalled the next time that the device is reenumerated.

6.  Plug in the device.

    Plug and Play will reenumerate the device, find the new driver for it, and install that driver.

