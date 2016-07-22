---
title: Porting code from SetupApi to CfgMgr32
description: This topic provides code examples that show how to port code that uses Setupapi.dll functionality to use Cfgmgr32.dll instead.
ms.assetid: 36668A17-EA56-464C-A38B-C75BE2359412
---

# Porting code from SetupApi to CfgMgr32


This topic provides code examples that show how to port code that uses Setupapi.dll functionality to use Cfgmgr32.dll instead. Porting your code allows you to run your code on the Universal Windows Platform (UWP), which does not support SetupApi. A subset of CfgMgr32 is supported on UWP, specifically functionality exposed through the api-ms-win-devices-config-l1-1-0.dll API set. To see a list of functions in this API set, please refer to [Windows API Sets](https://msdn.microsoft.com/library/windows/desktop/hh802935).

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

    ZeroMemory(&amp;DeviceInfoData, sizeof(DeviceInfoData));
    DeviceInfoData.cbSize = sizeof(DeviceInfoData);

    for (Index = 0;
         SetupDiEnumDeviceInfo(DeviceInfoSet,
                               Index,
                               &amp;DeviceInfoData);
         Index++)
    {
        // Query a property on the device.  For example, the device description.
        if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                      &amp;DeviceInfoData,
                                      &amp;DEVPKEY_Device_DeviceDesc,
                                      &amp;PropertyType,
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

This example gets a list of all present devices using [**CM\_Get\_Device\_ID\_List**](https://msdn.microsoft.com/library/windows/hardware/ff538415) and iterates through them to retrieve the device description of each device.

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

    cr = CM_Get_Device_ID_List_Size(&amp;DeviceListLength,
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
        cr = CM_Locate_DevNode(&amp;Devinst,
                               CurrentDevice,
                               CM_LOCATE_DEVNODE_NORMAL);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        PropertySize = sizeof(DeviceDesc);
        cr = CM_Get_DevNode_Property(Devinst,
                                     &amp;DEVPKEY_Device_DeviceDesc,
                                     &amp;PropertyType,
                                     (PBYTE)DeviceDesc,
                                     &amp;PropertySize,
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

## <a href="" id="get-a-list-of-interfaces--get-the-device-exposing-each-interface---and-get-a-property-from-the-device"></a>Get a list of interfaces, get the device exposing each interface, and get a property from the device


This example gets a list of all interfaces in class GUID\_DEVINTERFACE\_VOLUME using [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069). For each interface, it gets the device exposing the interface and gets a property of that device.

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

    DeviceInfoSet = SetupDiGetClassDevs(&amp;GUID_DEVINTERFACE_VOLUME,
                                        NULL,
                                        NULL,
                                        DIGCF_DEVICEINTERFACE);

    if (DeviceInfoSet == INVALID_HANDLE_VALUE)
    {
        goto Exit;
    }

    ZeroMemory(&amp;DeviceInterfaceData, sizeof(DeviceInterfaceData));
    DeviceInterfaceData.cbSize = sizeof(DeviceInterfaceData);

    for (Index = 0;
         SetupDiEnumDeviceInterfaces(DeviceInfoSet,
                                     NULL,
                                     &amp;GUID_DEVINTERFACE_VOLUME,
                                     Index,
                                     &amp;DeviceInterfaceData);
         Index++)
    {

        ZeroMemory(&amp;DeviceInfoData, sizeof(DeviceInfoData));
        DeviceInfoData.cbSize = sizeof(DeviceInfoData);

        if ((!SetupDiGetDeviceInterfaceDetail(DeviceInfoSet,
                                              &amp;DeviceInterfaceData,
                                              NULL,
                                              0,
                                              NULL,
                                              &amp;DeviceInfoData)) &amp;&amp;
            (GetLastError() != ERROR_INSUFFICIENT_BUFFER))
        {
            // The error can be retrieved with GetLastError();
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                      &amp;DeviceInfoData,
                                      &amp;DEVPKEY_Device_DeviceDesc,
                                      &amp;PropertyType,
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

This example gets a list of all interfaces in class GUID\_DEVINTERFACE\_VOLUME using [**CM\_Get\_Device\_Interface\_List**](https://msdn.microsoft.com/library/windows/hardware/ff538463). For each interface, it gets the device exposing the interface and gets a property of that device.

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

    cr = CM_Get_Device_Interface_List_Size(&amp;DeviceInterfaceListLength,
                                           (LPGUID)&amp;GUID_DEVINTERFACE_VOLUME,
                                           NULL,
                                           CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    DeviceInterfaceList = (PWSTR)HeapAlloc(GetProcessHeap(),
                                           HEAP_ZERO_MEMORY,
                                           DeviceInterfaceListLength * sizeof(WCHAR));

    if (DeviceInterfaceList == NULL)
    {
        goto Exit;
    }

    cr = CM_Get_Device_Interface_List((LPGUID)&amp;GUID_DEVINTERFACE_VOLUME,
                                      NULL,
                                      DeviceInterfaceList,
                                      DeviceInterfaceListLength,
                                      CM_GET_DEVICE_INTERFACE_LIST_ALL_DEVICES);

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
                                              &amp;DEVPKEY_Device_InstanceId,
                                              &amp;PropertyType,
                                              (PBYTE)CurrentDevice,
                                              &amp;PropertySize,
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
        cr = CM_Locate_DevNode(&amp;Devinst,
                               CurrentDevice,
                               CM_LOCATE_DEVNODE_PHANTOM);

        if (cr != CR_SUCCESS)
        {
            goto Exit;
        }

        // Query a property on the device.  For example, the device description.
        PropertySize = sizeof(DeviceDesc);
        cr = CM_Get_DevNode_Property(Devinst,
                                     &amp;DEVPKEY_Device_DeviceDesc,
                                     &amp;PropertyType,
                                     (PBYTE)DeviceDesc,
                                     &amp;PropertySize,
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

    ZeroMemory(&amp;DeviceInfoData, sizeof(DeviceInfoData));
    DeviceInfoData.cbSize = sizeof(DeviceInfoData);

    if (!SetupDiOpenDeviceInfo(DeviceInfoSet,
                               MY_DEVICE,
                               NULL,
                               0,
                               &amp;DeviceInfoData))
    {
        // The error can be retrieved with GetLastError();
        goto Exit;
    }

    // Query a property on the device.  For example, the device description.
    if (!SetupDiGetDeviceProperty(DeviceInfoSet,
                                  &amp;DeviceInfoData,
                                  &amp;DEVPKEY_Device_DeviceDesc,
                                  &amp;PropertyType,
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

This example takes a device instance path for a particular device and retrieves a property from it using [**CM\_Get\_DevNode\_Property**](https://msdn.microsoft.com/library/windows/hardware/hh780220).

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
    cr = CM_Locate_DevNode(&amp;Devinst,
                           MY_DEVICE,
                           CM_LOCATE_DEVNODE_NORMAL);

    if (cr != CR_SUCCESS)
    {
        goto Exit;
    }

    // Query a property on the device.  For example, the device description.
    PropertySize = sizeof(DeviceDesc);
    cr = CM_Get_DevNode_Property(Devinst,
                                 &amp;DEVPKEY_Device_DeviceDesc,
                                 &amp;PropertyType,
                                 (PBYTE)DeviceDesc,
                                 &amp;PropertySize,
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


This example shows how to disable a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF\_PROPERTYCHANGE**, specifying **DICS\_DISABLE**.

**Note**   By default, calling [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) results in the device staying disabled across reboots. To disable the device across reboots when calling [**CM\_Disable\_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff537996), you must specify the **CM\_DISABLE\_PERSIST** flag.

 

```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&amp;devinst,
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


This example shows how to enable a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF\_PROPERTYCHANGE**, specifying **DICS\_ENABLE**.

```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&amp;devinst,
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


This example shows how to restart a device using CfgMgr32. To do this with SetupApi, you would use [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with *InstallFunction* of **DIF\_PROPERTYCHANGE**, specifying **DICS\_PROPCHANGE**.

```ManagedCPlusPlus
    cr = CM_Locate_DevNode(&amp;devinst,
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Porting%20code%20from%20SetupApi%20to%20CfgMgr32%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




