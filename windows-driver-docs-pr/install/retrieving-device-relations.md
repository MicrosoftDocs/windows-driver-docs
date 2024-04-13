---
title: Retrieving Device Relations
description: Retrieving Device Relations
ms.date: 04/05/2022
---

# Retrieving Device Relations

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device relations properties. The unified device property model uses [property keys](property-keys.md) to represent these properties. The list of relations represented in the unified device property model are:
* [**DEVPKEY_Device_BusRelations**](devpkey-device-busrelations.md)
* [**DEVPKEY_Device_EjectionRelations**](devpkey-device-ejectionrelations.md)
* [**DEVPKEY_Device_PowerRelations**](devpkey-device-powerrelations.md)
* [**DEVPKEY_Device_RemovalRelations**](devpkey-device-removalrelations.md)
* [**DEVPKEY_Device_Parent**](devpkey-device-parent.md)
* [**DEVPKEY_Device_Children**](devpkey-device-children.md)
* [**DEVPKEY_Device_Siblings**](devpkey-device-siblings.md)

Windows Server 2003, Windows XP, and Windows 2000 do not support the property keys of the unified property model. However, you can retrieve the corresponding information by calling Plug and Play (PnP) configuration manager functions. To maintain compatibility with earlier Windows versions, Windows Vista and later versions also support calling PnP configuration manager functions to retrieve device relations properties. However, you should use the property keys of the unified device property model to access the device relation properties.For information about how to use property keys to access device driver properties, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

For information about how to access the device relations properties on Windows Server 2003, Windows XP, and Windows 2000, see the following topics:

[Retrieving Ejection Relations, Removal Relations, and Power Relations, and Bus Relations](#retrieving-ejection-relations-removal-relations-and-power-relations-and-bus-relations)

[Retrieving the Parent of a Device Instance](#retrieving-the-parent-of-a-device-instance)

[Retrieving the Children of a Device Instance](#retrieving-the-children-of-a-device-instance)

[Retrieving the Siblings of a Device Instance](#retrieving-the-siblings-of-a-device-instance)

## Retrieving Ejection Relations, Removal Relations, and Power Relations, and Bus Relations

To retrieve device relations information on Windows Server 2003, Windows XP, and Windows 2000, call **CM_Get_Device_ID_List** and supply the following parameter values:

-   Set *pszFilter* to a pointer to a NULL-terminated string that specifies the device instance identifier for which to retrieve relations information.

-   Set *Buffer* to a pointer to a buffer that receives a list of NULL-terminated device instance identifiers. The list is terminated by an additional NULL character. You can get the required buffer size by calling the **CM_Get_Device_ID_List_Size** function.

-   Set *BufferLen* to the size, in characters, of the *Buffer* buffer.

-   Set *ulFlags* to one of the following flags to retrieve the corresponding relations information:
    -   CM_GETIDLIST_FILTER_EJECTIONRELATIONS

        The CM_GETIDLIST_FILTER_EJECTIONRELATIONS flag retrieves [**ejection relations**](../kernel/irp-mn-query-device-relations.md), which is the same information that is provided by the [**DEVPKEY_Device_EjectionRelations**](./devpkey-device-ejectionrelations.md) device property in Windows Vista and later versions.

    -   CM_GETIDLIST_FILTER_REMOVALRELATIONS

        The CM_GETIDLIST_FILTER_REMOVALRELATIONS flag retrieves [**removal relations**](../kernel/irp-mn-query-device-relations.md), which is the same information that is provided by the [**DEVPKEY_Device_RemovalRelations**](./devpkey-device-removalrelations.md) device property in Windows Vista and later versions.

    -   CM_GETIDLIST_FILTER_POWERRELATIONS

        The CM_GETIDLIST_FILTER_POWERRELATIONS flag retrieves power relations, which is the same information that is provided by the [**DEVPKEY_Device_PowerRelations**](./devpkey-device-powerrelations.md) device property in Windows Vista and later versions.

    -   CM_GETIDLIST_FILTER_BUSRELATIONS

        The CM_GETIDLIST_FILTER_BUSRELATIONS flag retrieves [**bus relations**](../kernel/irp-mn-query-device-relations.md), which is the same information that is provided by the [**DEVPKEY_Device_BusRelations**](./devpkey-device-busrelations.md) device property in Windows Vista and later versions.

If the call to **CM_Get_Device_ID_List** succeeds, **CM_Get_Device_ID_List** retrieves the requested relations information and returns CR_SUCCESS. Otherwise, **CM_Get_Device_ID_List** returns one of the error codes with prefix "CR_" that are defined in *Cfgmgr32.h*.

## Retrieving the Parent of a Device Instance

To retrieve the device instance identifier of a parent device on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call the [**CM_Get_Parent**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_parent) function to retrieve a device instance handle to the parent device of a device instance.

2.  Call [**CM_Get_Device_ID**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw) to retrieve the device instance identifier that is associated with the device instance handle to the parent device that was retrieved by the previous call to **CM_Get_Parent**.

This information retrieved by using this procedure is the same as that represented by the [**DEVPKEY_Device_Parent**](devpkey-device-parent.md) property in the unified device property model of Windows Vista and later versions.

## Retrieving the Children of a Device Instance

To retrieve the device instance identifiers of the child devices of a device instance on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call the [**CM_Get_Child**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_child) function to retrieve a device instance handle to the first child device that is associated with a device instance.

2.  Call [**CM_Get_Sibling**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_sibling) as many times as it is necessary to enumerate all the sibling devices of the first child device that was retrieved by the call to **CM_Get_Child**.

3.  Call **CM_Get_Device_ID** to retrieve the device instance identifiers that are associated with the device instance handles that were returned by the calls to **CM_Get_Child** and **CM_Get_Sibling**.

This information retrieved by using this procedure is the same as that represented by the [**DEVPKEY_Device_Children**](devpkey-device-children.md) property in the unified device property model of Windows Vista and later versions.

## Retrieving the Siblings of a Device Instance

To retrieve the device instance identifiers of the sibling devices of device instance Abc on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call the [**CM_Get_Parent**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_parent) function to retrieve a device instance handle to the parent device of device instance *Abc*.

2.  Call the [**CM_Get_Child**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_child) function to retrieve a device instance handle to the first child device of the parent device of device instance *Abc*.

3.  Call [**CM_Get_Sibling**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_sibling) as many times as is necessary to enumerate all the sibling devices of the first child device of the parent device. This enumeration will also return a handle to device instance *Abc*.

4.  Call [**CM_Get_Device_ID**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw) to retrieve the device instance identifiers that are associated with the device instance handles that were returned by the previous calls to **CM_Get_Sibling**. Remove the handle to device instance *Abc* from the list of sibling devices of the first child device of the parent device.

The information retrieved by using this procedure is the same as that represented by the [**DEVPKEY_Device_Siblings**](devpkey-device-siblings.md) property in the unified device property model of Windows Vista and later versions. If a **CM_<em>Xxx</em>** function call listed in this section succeeds, the **CM_<em>Xxx</em>** function retrieves the requested information and returns CR_SUCCESS. Otherwise, the **CM_<em>Xxx</em>** function returns one of the error codes with prefix "CR_" that are defined in *Cfgmgr32.h*.
