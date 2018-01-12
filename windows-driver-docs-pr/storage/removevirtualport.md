---
title: RemoveVirtualPort method
description: The RemoveVirtualPort method removes a virtual port for a specific world wide port name (WWPN) .
ms.assetid: 47A85B72-821C-4552-BA6E-1742D58B54A4
keywords: ["RemoveVirtualPort method Storage Devices"]
topic_type:
- apiref
api_name:
- RemoveVirtualPort
api_type:
- COM
---

# RemoveVirtualPort method


The **RemoveVirtualPort** method removes a virtual port for a specific world wide port name (WWPN) .

Syntax
------

```ManagedCPlusPlus
void RemoveVirtualPort(
   [in] uint8   WWPN[8],
   [out] uint16 Status
);
```

Parameters
----------

*WWPN\[8\]*   
The world wide port name of the virtual port to remove.

*Status*   
On return, contains the status of the operation.

Return value
------------

Not applicable to WMI methods.

## <span id="see_also"></span>See also


[NPIV Status Codes](https://msdn.microsoft.com/library/windows/hardware/dn386176)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20RemoveVirtualPort%20method%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





