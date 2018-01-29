---
title: DriverEntry of IDE Controller Minidriver function
description: DriverEntry initializes the minidriver.
ms.assetid: 124f6273-ab15-426b-abce-a4d8e68e09c7
keywords: ["DriverEntry function Storage Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
---

# DriverEntry of IDE Controller Minidriver function


**DriverEntry** initializes the minidriver.

Syntax
------

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

Parameters
----------

*DriverObject* \[in\]  
Contains a pointer to the IDE controller minidriver's driver object.

*RegistryPath* \[in\]  
Specifies a string indicating the registry path to the driver's configuration information in the registry.

Return value
------------

**DriverEntry** returns STATUS\_SUCCESS if successful; otherwise it returns the error code received from the [**PciIdeXInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff563788) library routine.

Remarks
-------

Each controller minidriver must have a routine named **DriverEntry** in order to load.

An IDE controller minidriver's **DriverEntry** routine must call the [**PciIdeXInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff563788) library routine. **PciIdeXInitialize** initializes the controller minidriver's dispatch tables, allocates an extension for the *DriverObject*, and stores various values in the driver object's extension. Values that must be stored in the driver object's extension include the size of the driver extension and a pointer to a controller minidriver [**HwIdeXGetControllerProperties**](https://msdn.microsoft.com/library/windows/hardware/ff557254) routine that retrieves information about the IDE controller.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ide.h (include Ide.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**HwIdeXGetControllerProperties**](https://msdn.microsoft.com/library/windows/hardware/ff557254)

[**IDE\_CONTROLLER\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff559076)

[**PciIdeXInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff563788)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DriverEntry%20of%20IDE%20Controller%20Minidriver%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





