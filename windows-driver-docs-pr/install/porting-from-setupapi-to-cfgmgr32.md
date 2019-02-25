---
title: Porting code from SetupApi to CfgMgr32
description: This topic provides code examples that show how to port code that uses Setupapi.dll functionality to use Cfgmgr32.dll instead.
ms.assetid: 36668A17-EA56-464C-A38B-C75BE2359412
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting code from SetupApi to CfgMgr32


This topic provides code examples that show how to port code that uses Setupapi.dll functionality to use Cfgmgr32.dll instead. Porting your code allows you to run your code on the Universal Windows Platform (UWP), which does not support SetupApi. A subset of CfgMgr32 is supported on UWP, specifically functionality exposed through the `api-ms-win-devices-config-l1-1-0.dll` API set (Windows 8 and later) or the `api-ms-win-devices-config-l1-1-1.dll` API set (Windows 8.1 and later). In Windows 10 and later, simply link to `onecore.lib`.

To see a list of functions in the above API sets, please refer to [Windows API Sets](https://msdn.microsoft.com/library/windows/desktop/hh802935) or [Onecore.lib: APIs from api-ms-win-devices-config-l1-1-1.dll](https://msdn.microsoft.com/library/windows/desktop/mt654039#_api-ms-win-devices-config-l1-1-1.dll).

The following sections include code examples that applications would typically use.

-   [Get a list of present devices and retrieve a property for each device](#get-a-list-of-present-devices-and-retrieve-a-property-for-each-device)
-   [Get a list of interfaces, get the device exposing each interface, and get a property from the device](#get-a-list-of-interfaces--get-the-device-exposing-each-interface---and-get-a-property-from-the-device)
-   [Get a property from a specific device](#get-a-property-from-a-specific-device)
-   [Disable device](#disable-device)
-   [Enable device](#enable-device)
-   [Restart device](#restart-device)

## Get a list of present devices and retrieve a property for each device


This example gets a list of all present devices using [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) and iterates through them to retrieve the device description of each device.

```ManagedCPlusPlus
VOID
GetDevicePropertiesSetupapi(
    VOID
    )
{
    HDEVINFO DeviceInfoSet = INVALID_HANDLE_VALUE;
    SP_DEVINFO_DATA DeviceInfoData;
    DWORD Index;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;

    DeviceInfoSet = SetupDiGetClassDevs(NULL,
                                        NULL,
                                        NULL,
                                        DIGCF_ALLCLASSES | DIGCF_PRESENT);

    if (DeviceInfoSet == INVALID_HANDLE_VALUE)
    {
        goto Exit;
    }

    ZeroMemory(&DeviceInfoData, sizeof(DeviceInfoData));
    DeviceInfoData.cbSize = sizeof(DeviceInfoData);

    for (Index = 0;
         SetupDiEnumDeviceInfo(DeviceInfoSet,
                               Index,
                               &DeviceInfoData);
         Index++)
    {
        // Query a property on the device.  For example, the device description.
        if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                      &DeviceInfoData,
                                      &DEVPKEY_Device_DeviceDesc,
                                      &PropertyType,
                                      (PBYTE)DeviceDesc,
                                      sizeof(DeviceDesc),
                                      NULL,
                                      0))
        {
            // The error can be retrieved with GetLastError();
            continue;
        }

        if (PropertyType != DEVPROP_TYPE_STRING)
        {
            continue;
        }
    }

    if (GetLastError() != ERROR_NO_MORE_ITEMS)
    {
        goto Exit;
    }

  Exit:

    if (DeviceInfoSet != INVALID_HANDLE_VALUE)
    {
        SetupDiDestroyDeviceInfoList(DeviceInfoSet);
    }

    return;
}
```

This example gets a list of all present devices using [**CM_Get_Device_ID_List**](https://msdn.microsoft.com/library/windows/hardware/ff538415) and iterates through them to retrieve the device description of each device.

```ManagedCPlusPlus
VOID
GetDevicePropertiesCfgmgr32(
    VOID
    )
{
    CONFIGRET cr = CR_SUCCESS;
    PWSTR DeviceList = NULL;
    ULONG DeviceListLength = 0;
    PWSTR CurrentDevice;
    DEVINST Devinst;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;
    ULONG PropertySize;
    DWORD Index = 0;

    cr = CM_Get_Device_ID_List_Size(&DeviceListLength,
                                    NULL,
                                    CM_GETIDLIST_FILTER_PRESENT);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    DeviceList = (PWSTR)HeapAlloc(GetProcessHeap(),
                                  HEAP_ZERO_MEMORY,
                                  DeviceListLength * sizeof(WCHAR));

    if (DeviceList == NULL) {
        goto Exit;
    }

    cr = CM_Get_Device_ID_List(NULL,
                               DeviceList,
                               DeviceListLength,
                               CM_GETIDLIST_FILTER_PRESENT);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    for (CurrentDevice = DeviceList;
         *CurrentDevice;
         CurrentDevice += wcslen(CurrentDevice) + 1)
    {

        // If the list of devices also includes non-present devices,
        // CM_LOCATE_DEVNODE_PHANTOM should be used in place of
        // CM_LOCATE_DEVNODE_NORMAL.
        cr = CM_Locate_DevNode(&Devinst,
                               CurrentDevice,
                               CM_LOCATE_DEVNODE_NORMAL);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        PropertySize = sizeof(DeviceDesc);
        cr = CM_Get_DevNode_Property(Devinst,
                                     &DEVPKEY_Device_DeviceDesc,
                                     &PropertyType,
                                     (PBYTE)DeviceDesc,
                                     &PropertySize,
                                     0);

        if (cr != CR_SUCCESS)
        {
            Index++;
            continue;
        }

        if (PropertyType != DEVPROP_TYPE_STRING)
        {
            Index++;
            continue;
        }

        Index++;
    }

  Exit:

    if (DeviceList != NULL)
    {
        HeapFree(GetProcessHeap(),
                 0,
                 DeviceList);
    }

    return;
}
```

## Get a list of interfaces, get the device exposing each interface, and get a property from the device


This example gets a list of all interfaces in class GUID_DEVINTERFACE_VOLUME using [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069). For each interface, it gets the device exposing the interface and gets a property of that device.

```ManagedCPlusPlus
VOID
GetInterfacesAndDevicePropertySetupapi(
    VOID
    )
{
    HDEVINFO DeviceInfoSet = INVALID_HANDLE_VALUE;
    SP_DEVICE_INTERFACE_DATA DeviceInterfaceData;
    SP_DEVINFO_DATA DeviceInfoData;
    DWORD Index;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;

    DeviceInfoSet = SetupDiGetClassDevs(&GUID_DEVINTERFACE_VOLUME,
                                        NULL,
                                        NULL,
                                        DIGCF_DEVICEINTERFACE);

    if (DeviceInfoSet == INVALID_HANDLE_VALUE)
    {
        goto Exit;
    }

    ZeroMemory(&DeviceInterfaceData, sizeof(DeviceInterfaceData));
    DeviceInterfaceData.cbSize = sizeof(DeviceInterfaceData);

    for (Index = 0;
         SetupDiEnumDeviceInterfaces(DeviceInfoSet,
                                     NULL,
                                     &GUID_DEVINTERFACE_VOLUME,
                                     Index,
                                     &DeviceInterfaceData);
         Index++)
    {

        ZeroMemory(&DeviceInfoData, sizeof(DeviceInfoData));
        DeviceInfoData.cbSize = sizeof(DeviceInfoData);

        if ((!SetupDiGetDeviceInterfaceDetail(DeviceInfoSet,
                                              &DeviceInterfaceData,
                                              NULL,
                                              0,
                                              NULL,
                                              &DeviceInfoData)) &&
            (GetLastError() != ERROR_INSUFFICIENT_BUFFER))
        {
            // The error can be retrieved with GetLastError();
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                      &DeviceInfoData,
                                      &DEVPKEY_Device_DeviceDesc,
                                      &PropertyType,
                                      (PBYTE)DeviceDesc,
                                      sizeof(DeviceDesc),
                                      NULL,
                                      0))
        {
            // The error can be retrieved with GetLastError();
            goto Exit;
        }

        if (PropertyType != DEVPROP_TYPE_STRING)
        {
            goto Exit;
        }
    }

    if (GetLastError() != ERROR_NO_MORE_ITEMS)
    {
        goto Exit;
    }

  Exit:

    if (DeviceInfoSet != INVALID_HANDLE_VALUE)
    {
        SetupDiDestroyDeviceInfoList(DeviceInfoSet);
    }

    return;
}
```

This example gets a list of all interfaces in class GUID_DEVINTERFACE_VOLUME using [**CM_Get_Device_Interface_List**](https://msdn.microsoft.com/library/windows/hardware/ff538463). For each interface, it gets the device exposing the interface and gets a property of that device.

```ManagedCPlusPlus
VOID
GetInterfacesAndDevicePropertyCfgmgr32(
    VOID
    )
{
    CONFIGRET cr = CR_SUCCESS;
    PWSTR DeviceInterfaceList = NULL;
    ULONG DeviceInterfaceListLength = 0;
    PWSTR CurrentInterface;
    WCHAR CurrentDevice[MAX_DEVICE_ID_LEN];
    DEVINST Devinst;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;
    ULONG PropertySize;
    DWORD Index = 0;

    do {
        cr = CM_Get_Device_Interface_List_Size(&DeviceInterfaceListLength,
                                               (LPGUID)&GUID_DEVINTERFACE_VOLUME,
                                               NULL,
                                               CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);

        if (cr != CR_SUCCESS)
        {
            break;
        }

        if (DeviceInterfaceList != NULL) {
            HeapFree(GetProcessHeap(),
                     0,
                     DeviceInterfaceList);
        }

        DeviceInterfaceList = (PWSTR)HeapAlloc(GetProcessHeap(),
                                               HEAP_ZERO_MEMORY,
                                               DeviceInterfaceListLength * sizeof(WCHAR));

        if (DeviceInterfaceList == NULL)
        {
            cr = CR_OUT_OF_MEMORY;
            break;
        }

        cr = CM_Get_Device_Interface_List((LPGUID)&GUID_DEVINTERFACE_VOLUME,
                                          NULL,
                                          DeviceInterfaceList,
                                          DeviceInterfaceListLength,
                                          CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);
    } while (cr == CR_BUFFER_SMALL);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    for (CurrentInterface = DeviceInterfaceList;
         *CurrentInterface;
         CurrentInterface += wcslen(CurrentInterface) + 1)
    {

        PropertySize = sizeof(CurrentDevice);
        cr = CM_Get_Device_Interface_Property(CurrentInterface,
                                              &DEVPKEY_Device_InstanceId,
                                              &PropertyType,
                                              (PBYTE)CurrentDevice,
                                              &PropertySize,
                                              0);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        if (PropertyType != DEVPROP_TYPE_STRING)
        {
            goto Exit;
        }

        // Since the list of interfaces includes all interfaces, enabled or not, the
        // device that exposed that interface may currently be non-present, so
        // CM_LOCATE_DEVNODE_PHANTOM should be used.
        cr = CM_Locate_DevNode(&Devinst,
                               CurrentDevice,
                               CM_LOCATE_DEVNODE_PHANTOM);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        PropertySize = sizeof(DeviceDesc);
        cr = CM_Get_DevNode_Property(Devinst,
                                     &DEVPKEY_Device_DeviceDesc,
                                     &PropertyType,
                                     (PBYTE)DeviceDesc,
                                     &PropertySize,
                                     0);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        if (PropertyType != DEVPROP_TYPE_STRING)
        {
            goto Exit;
        }

        Index++;
    }

  Exit:

    if (DeviceInterfaceList != NULL)
    {
        HeapFree(GetProcessHeap(),
                 0,
                 DeviceInterfaceList);
    }

    return;
}
```

## Get a property from a specific device


This example takes a device instance path for a particular device and retrieves a property from it using [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

```ManagedCPlusPlus
VOID
GetDevicePropertySpecificDeviceSetupapi(
    VOID
    )
{
    HDEVINFO DeviceInfoSet = INVALID_HANDLE_VALUE;
    SP_DEVINFO_DATA DeviceInfoData;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;

    DeviceInfoSet = SetupDiCreateDeviceInfoList(NULL, NULL);

    if (DeviceInfoSet == INVALID_HANDLE_VALUE)
    {
        goto Exit;
    }

    ZeroMemory(&DeviceInfoData, sizeof(DeviceInfoData));
    DeviceInfoData.cbSize = sizeof(DeviceInfoData);

    if (!SetupDiOpenDeviceInfo(DeviceInfoSet,
                               MY_DEVICE,
                               NULL,
                               0,
                               &DeviceInfoData))
    {
        // The error can be retrieved with GetLastError();
        goto Exit;
    }

    // Query a property on the device.  For example, the device description.
    if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                  &DeviceInfoData,
                                  &DEVPKEY_Device_DeviceDesc,
                                  &PropertyType,
                                  (PBYTE)DeviceDesc,
                                  sizeof(DeviceDesc),
                                  NULL,
                                  0)) {
        // The error can be retrieved with GetLastError();
        goto Exit;
    }

    if (PropertyType != DEVPROP_TYPE_STRING)
    {
        goto Exit;
    }

  Exit:

    if (DeviceInfoSet != INVALID_HANDLE_VALUE)
    {
        SetupDiDestroyDeviceInfoList(DeviceInfoSet);
    }

    return;
}
```

This example takes a device instance path for a particular device and retrieves a property from it using [**CM_Get_DevNode_Property**](https://msdn.microsoft.com/library/windows/hardware/hh780220).

```ManagedCPlusPlus
void
GetDevicePropertySpecificDeviceCfgmgr32(
    VOID
    )
{
    CONFIGRET cr = CR_SUCCESS;
    DEVINST Devinst;
    WCHAR DeviceDesc[2048];
    DEVPROPTYPE PropertyType;
    ULONG PropertySize;

    // If MY_DEVICE could be a non-present device, CM_LOCATE_DEVNODE_PHANTOM
    // should be used in place of CM_LOCATE_DEVNODE_NORMAL.
    cr = CM_Locate_DevNode(&Devinst,
                           MY_DEVICE,
                           CM_LOCATE_DEVNODE_NORMAL);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    // Query a property on the device.  For example, the device description.
    PropertySize = sizeof(DeviceDesc);
    cr = CM_Get_DevNode_Property(Devinst,
                                 &DEVPKEY_Device_DeviceDesc,
                                 &PropertyType,
                                 (PBYTE)DeviceDesc,
                                 &PropertySize,
                                 0);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    if (PropertyType != DEVPROP_TYPE_STRING)
    {
        goto Exit;
    }

  Exit:

    return;
}
```

## Disable device


This example shows how to disable a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF_PROPERTYCHANGE**, specifying **DICS_DISABLE**.

**Note**   By default, calling [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) results in the device staying disabled across reboots. To disable the device across reboots when calling [**CM_Disable_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff537996), you must specify the **CM_DISABLE_PERSIST** flag.



```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&devinst,
                           (DEVINSTID_W)DeviceInstanceId,
                           CM_LOCATE_DEVNODE_NORMAL);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }

    cr = CM_Disable_DevNode(devinst, 0);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }
```

## Enable device


This example shows how to enable a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF_PROPERTYCHANGE**, specifying **DICS_ENABLE**.

```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&devinst,
                           (DEVINSTID_W)DeviceInstanceId,
                           CM_LOCATE_DEVNODE_NORMAL);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }

    cr = CM_Enable_DevNode(devinst, 0);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }
```

## Restart device


This example shows how to restart a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF_PROPERTYCHANGE**, specifying **DICS_PROPCHANGE**.

```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&devinst,
                           (DEVINSTID_W)DeviceInstanceId,
                           CM_LOCATE_DEVNODE_NORMAL);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }

    cr = CM_Query_And_Remove_SubTree(devinst,
                                     NULL,
                                     NULL,
                                     0,
                                     CM_REMOVE_NO_RESTART);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }

    cr = CM_Setup_DevNode(devinst,
                          CM_SETUP_DEVNODE_READY);

    if (cr != CR_SUCCESS) {
        goto Exit;
    }
```









