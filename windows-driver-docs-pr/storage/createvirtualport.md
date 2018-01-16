---
title: CreateVirtualPort method
description: The CreateVirtualPort method creates a virtual port with a specific world wide port name (WWPN) .
ms.assetid: B4274FB7-2850-4E17-ACDE-5592B0390E8B
keywords: ["CreateVirtualPort method Storage Devices"]
topic_type:
- apiref
api_name:
- CreateVirtualPort
api_type:
- COM
---

# CreateVirtualPort method


The **CreateVirtualPort** method creates a virtual port with a specific world wide port name (WWPN) .

Syntax
------

```ManagedCPlusPlus
void CreateVirtualPort(
   [in] uint8   WWPN[8],
   [in] uint8   WWNN[8],
   [in] uint8   Tag[16],
   [in] uint16  VirtualName[64],
   [out] uint16 Status
);
```

Parameters
----------

*WWPN\[8\]*   
The world wide port name of the virtual port to create.

*WWNN\[8\]*   
The world wide node name to associate with the virtual port.

*Tag\[16\]*   
A tag identifier for the virtual port.

*VirtualName\[64\]*   
A symbolic name for the virtual port.

*Status*   
On return, contains the status of the operation.

Return value
------------

Not applicable to WMI methods.

## <span id="see_also"></span>See also


[NPIV Status Codes](https://msdn.microsoft.com/library/windows/hardware/dn386176)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20CreateVirtualPort%20method%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





