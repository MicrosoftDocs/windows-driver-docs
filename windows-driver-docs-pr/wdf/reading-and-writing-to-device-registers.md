---
title: Reading and Writing to Device Registers
description: Reading and Writing to Device Registers
ms.assetid: 58A94C75-94C1-4517-A300-9F04AA7B771A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading and Writing to Device Registers


After a driver has mapped registers as described in [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md), a KMDF driver uses the [**HAL Library Routines**](https://msdn.microsoft.com/library/windows/hardware/ff546644) to read and write to registers, while a UMDF driver (version 2.0 or later) typically uses the [WDF Register/Port Access Functions](https://msdn.microsoft.com/library/windows/hardware/dn265662).

If a UMDF driver needs to access memory-mapped registers directly, it can set the INF directive **UmdfRegisterAccessMode** to **RegisterAccessUsingUserModeMapping** and then call [**WdfDeviceGetHardwareRegisterMappedAddress**](https://msdn.microsoft.com/library/windows/hardware/dn265603) to retrieve a user-mode mapped address. Because the framework doesn't validate read and write accesses performed in this way, this technique is not recommended for register access. For a complete list of UMDF INF directives, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

The following example includes code that could be compiled using KMDF (1.13 or later) or UMDF (2.0 or later). The example shows how a driver uses its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function to examine its memory-mapped register resources and map them into user-mode address space. The example then demonstrates how to access the memory locations.

Before accessing device registers and ports, a UMDF driver must set the **UmdfDirectHardwareAccess** directive to **AllowDirectHardwareAccess** in the driver's INF file.

```cpp
NTSTATUS
 MyDevicePrepareHardware (
    IN WDFDEVICE  Device,
    IN WDFCMRESLIST  ResourcesRaw,
    IN WDFCMRESLIST  ResourcesTranslated
    )
  
{
    PCM_PARTIAL_RESOURCE_DESCRIPTOR desc = NULL;
    PCM_PARTIAL_RESOURCE_DESCRIPTOR  descTranslated = NULL;
    PHYSICAL_ADDRESS regBasePA = {0};
    ULONG regLength = 0;
    BOOLEAN found = FALSE;
    ULONG  i;
    PFDO_DATA deviceContext;
    NTSTATUS status = STATUS_SUCCESS;
    
    UNREFERENCED_PARAMETER(ResourcesRaw);

    MyKdPrint(("MyEvtDevicePrepareHardware Device 0x%p ResRaw 0x%p ResTrans "
        "0x%p Count %d\n", Device, ResourcesRaw, ResourcesTranslated,
        WdfCmResourceListGetCount(ResourcesTranslated)));

#ifndef _KERNEL_MODE
    WDF_DEVICE_IO_TYPE stackReadWriteIotype = WdfDeviceIoUndefined; 
    WDF_DEVICE_IO_TYPE stackIoctlIotype = WdfDeviceIoUndefined;
    WdfDeviceGetDeviceStackIoType(Device,
                                  &stackReadWriteIotype,
                                  &stackIoctlIotype);
    MyKdPrint(("Device 0x%p stackReadWriteIoType %S stackIoctlIoType %S\n",
        Device,
        GetIoTypeName(stackReadWriteIotype),
        GetIoTypeName(stackIoctlIotype)
        ));

#endif

    deviceContext = ToasterFdoGetData(Device);
    
    //
    // Scan the list and identify our resource
    //
    for (i = 0; i < WdfCmResourceListGetCount(ResourcesTranslated); i++) {
        desc = WdfCmResourceListGetDescriptor(Resources, i);
        descTranslated =  WdfCmResourceListGetDescriptor(ResourcesTranslated, i);
           
        switch (desc->Type) {
            case CmResourceTypeMemory:
                MyKdPrint(("EvtPrepareHardware: found CmResourceTypeMemory resources \n"));
                //
                // see if this is the memory resource we&#39;re looking for
                // 
                if (desc->u.Memory.Length == 0x200) {
                    regBasePA = desc->u.Memory.Start;
                    regLength = desc->u.Memory.Length;
                    found = TRUE;                    
                }
                break;
                
            case CmResourceTypePort:
                MyKdPrint(("EvtPrepareHardware: found CmResourceTypePort"
                    " resource\n"));

                switch(descTranslated->Type) {

                case CmResourceTypePort:
                    deviceContext->PortWasMapped = FALSE;
                    deviceContext->PortBase = 
                        ULongToPtr(descTranslated->u.Port.Start.LowPart);
                    deviceContext->PortCount = descTranslated ->u.Port.Length;
                    MyKdPrint(("Resource Translated Port: (%x) Length: (%d)\n",
                             descTranslated->u.Port.Start.LowPart,
                             descTranslated->u.Port.Length));                        
                    break;
                    
                case CmResourceTypeMemory:
                    //
                    // Map the memory
                    //

#if IS_UMDF_DRIVER                    
                    status = WdfDeviceMapIoSpace(
                                            Device,
                                            descTranslated->u.Memory.Start,
                                            descTranslated->u.Memory.Length,
                                            MmNonCached,
                                            &deviceContext->PortBase
                                            );

                    if (!NT_SUCCESS(status)) {
                        WdfVerifierDbgBreakPoint();
                    }
#else
                    deviceContext->PortBase = (PVOID) 
                                        MmMapIoSpace(
                                            descTranslated->u.Memory.Start,
                                            descTranslated->u.Memory.Length,
                                            MmNonCached
                                            );
                    UNREFERENCED_PARAMETER(status);

#endif
                    deviceContext->PortCount = descTranslated->u.Memory.Length;
                    deviceContext->PortWasMapped = TRUE;
                    MyKdPrint(("Resource Translated Memory: (%x) Length: (%d)\n",
                             descTranslated->u.Memory.Start.LowPart,
                             descTranslated->u.Memory.Length));                        
                    break;
                default:
                    MyKdPrint(("Unhandled resource_type (0x%x)\n", 
                        descTranslated->Type));
                }
                break;

            case CmResourceTypeInterrupt:
                MyKdPrint(("EvtPrepareHardware: found CmResourceTypeInterrupt"
                    "resource\n"));
                break;                

            case CmResourceTypeConnection:
                MyKdPrint(("EvtPrepareHardware: found CmResourceTypeConnection"
                    "resource\n"));
                break;                

            default:
                MyKdPrint(("EvtPrepareHardware: found resources of type %d"
                    "(CM_RESOURCE_TYPE)\n", desc->Type));
                break;
        }
    }


//
// Next, the driver uses register/port access macros to access the port.
//

    if ((PUCHAR)&deviceContext->PortBase != NULL) {
        UCHAR data;
        
#ifndef _KERNEL_MODE
        data = WDF_READ_PORT_UCHAR(Device, (PUCHAR)deviceContext->PortBase);
#else
        data = READ_PORT_UCHAR((PUCHAR)deviceContext->PortBase);
#endif

        MyKdPrint(("Read value %d from port address 0x%p\n", data, 
            deviceContext->PortBase));
    }
  
  if (i == 0) {
        MyKdPrint(("EvtPrepareHardware: no cm resources found \n"));
    }
    
    return STATUS_SUCCESS;
}



NTSTATUS
 MyDeviceReleaseHardware (
    IN WDFDEVICE  Device,
    IN WDFCMRESLIST  ResourcesTranslated
    )

{
    PFDO_DATA deviceContext;

    UNREFERENCED_PARAMETER(ResourcesTranslated);

    MyKdPrint(("CovEvtDeviceReleaseHardware Device 0x%p ResTrans 0x%p\n", 
        Device, ResourcesTranslated));

    deviceContext = ToasterFdoGetData(Device);

    if (deviceContext->PortWasMapped) {
#if IS_UMDF_DRIVER
        WdfDeviceUnmapIoSpace(Device,
                              deviceContext->PortBase,
                              deviceContext->PortCount);
#else
        MmUnmapIoSpace(deviceContext->PortBase,
                     deviceContext->PortCount);
#endif
    }

    return STATUS_SUCCESS;
}
```

 

 





