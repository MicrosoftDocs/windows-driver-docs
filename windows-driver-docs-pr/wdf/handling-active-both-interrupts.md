---
title: Handling Active-Both Interrupts
description: Handling Active-Both Interrupts
ms.assetid: CFA205B1-FDDD-4E27-8CF9-106C8D1CC4EF
---

# Handling Active-Both Interrupts


**Note**  This topic applies only to Kernel-Mode Driver Framework (KMDF) version 1.13 and earlier.

 

Many devices have hardware registers that control interrupt generation and masking. Typically, KMDF and UMDF drivers for such devices use the framework's built-in interrupt support.

However, a simple device on a System on a Chip (SoC) hardware platform might not have hardware registers for interrupts. As a result, a driver for such a device might not be able to control when the interrupt gets generated, or be able to mask the interrupt in hardware. If the device interrupts immediately upon connection, and the driver is using the framework's interrupt support, it is possible for the interrupt to fire before the framework has fully initialized the framework interrupt object. As a result, a KMDF driver must call WDM routines directly to connect and disconnect interrupts. Because a UMDF driver cannot call these methods, you cannot write a UMDF driver for such a device.

This topic describes how a KMDF driver might handle interrupts for such a device.

On SoC hardware platforms, active-both interrupts are typically used for very simple devices like hardware push-buttons. When a user presses a push-button, the interrupt signal line from the device transitions from low to high, or from high to low. When the user releases the push-button, the interrupt line transitions in the opposite direction. A GPIO pin configured as an active-both interrupt input generates interrupts on both low-to-high and high-to-low transitions, resulting in the system calling the peripheral device driver's interrupt service routine (ISR) in both cases. However, the driver does not receive an indication whether the transition is low-to-high or high-to-low.

To distinguish between low-to-high and high-to-low transitions, the driver must track the state of each interrupt. To do so, your driver might maintain a Boolean interrupt state value that is **FALSE** when interrupt line state is low and **TRUE** when line state is high.

Consider an example in which the line state defaults to low when the system starts. The driver initializes the state value to **FALSE** in its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function. Then each time the driver's ISR is called, signaling a change in state, the driver inverts the state value in its ISR.

If the line state is high when the system starts, the interrupt fires immediately after it is enabled. Because the driver calls the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine directly, instead of calling [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345), it is ensured of receiving a possible immediate interrupt.

This solution requires that the GPIO controller support active-both interrupts in hardware, or that the driver for the GPIO controller emulate active-both interrupts in software. For information about emulating active-both interrupts, see the description of the **EmulateActiveBoth** member of the [**CONTROLLER\_ATTRIBUTE\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh439449) structure.

The following code example shows how a KMDF driver for a peripheral device can track interrupt polarity.

```
typedef struct _INTERRUPT_CONTEXT INTERRUPT_CONTEXT, *PINTERRUPT_CONTEXT;
typedef struct _DEVICE_CONTEXT DEVICE_CONTEXT, *PDEVICE_CONTEXT;


struct _INTERRUPT_CONTEXT
{
               BOOLEAN State;
               PDEVICE_CONTEXT DeviceContext;
};

struct _DEVICE_CONTEXT
{
               PKINTERRUPT Interrupt;
               INTERRUPT_CONTEXT InterruptContext;
               PDEVICE_OBJECT PhysicalDeviceObject;
               KSPIN_LOCK SpinLock;
};

...

BOOLEAN
YourInterruptIsr(
               __in PKINTERRUPT Interrupt,
               __in PVOID ServiceContext
               )
{
               PINTERRUPT_CONTEXT InterruptContext = (PINTERRUPT_CONTEXT)ServiceContext;
               PDEVICE_CONTEXT DeviceContext = InterruptContext->DeviceContext;

               //
               // Flip the state.
               //
               InterruptContext->State = !InterruptContext->State;

               IoRequestDpc(DeviceContext->PhysicalDeviceObject, DeviceContext->PhysicalDeviceObject->CurrentIrp, InterruptContext);
}

VOID
YourInterruptDpc(
               __in PKDPC Dpc,
               __in PDEVICE_OBJECT DeviceObject,
               __inout PIRP Irp,
               __in_opt PVOID ContextPointer
               )
{
               PINTERRUPT_CONTEXT InterruptContext = (PINTERRUPT_CONTEXT)ContextPointer;

               ...
}

NTSTATUS
EvtDriverDeviceAdd(
               __in  WDFDRIVER Driver,
               __in  PWDFDEVICE_INIT DeviceInit
               )
{
               WDFDEVICE Device;
               PDEVICE_CONTEXT DeviceContext;

               ...

               DeviceContext->Interrupt = NULL;
               DeviceContext->PhysicalDeviceObject = WdfDeviceWdmGetPhysicalDevice(Device);
               KeInitializeSpinLock(&amp;DeviceContext->SpinLock);

               IoInitializeDpcRequest(DeviceContext->PhysicalDeviceObject, YourInterruptDpc);
}

NTSTATUS
EvtDevicePrepareHardware(
               __in  WDFDEVICE Device,
               __in  WDFCMRESLIST ResourcesRaw,
               __in  WDFCMRESLIST ResourcesTranslated
               )
{
               PDEVICE_CONTEXT DeviceContext = YourGetDeviceContext(Device);

               for (ULONG i = 0; i < WdfCmResourceListGetCount(ResourcesTranslated); i++)
               {
                              PCM_PARTIAL_RESOURCE_DESCRIPTOR descriptor = WdfCmResourceListGetDescriptor(ResourcesTranslated, i);

                              if (descriptor->Type == CmResourceTypeInterrupt)
                              {
                                             IO_CONNECT_INTERRUPT_PARAMETERS params;
                                             RtlZeroMemory(&amp;params, sizeof(params));

                                             params.Version = CONNECT_FULLY_SPECIFIED;
                                             params.FullySpecified.PhysicalDeviceObject = DeviceContext->PhysicalDeviceObject;
                                             params.FullySpecified.InterruptObject = &amp;DeviceContext->Interrupt;
                                             params.FullySpecified.ServiceRoutine = YourInterruptIsr;
                                             params.FullySpecified.ServiceContext = (PVOID)&amp;DeviceContext->InterruptContext;
                                             params.FullySpecified.SpinLock = &amp;DeviceContext->SpinLock;
                                             params.FullySpecified.Vector = descriptor->u.Interrupt.Vector;
                                             params.FullySpecified.Irql = (KIRQL)descriptor->u.Interrupt.Level;
                                             params.FullySpecified.SynchronizeIrql = (KIRQL)descriptor->u.Interrupt.Level;
                                             params.FullySpecified.InterruptMode = (descriptor->Flags &amp; CM_RESOURCE_INTERRUPT_LATCHED) ? Latched : LevelSensitive;
                                             params.FullySpecified.ProcessorEnableMask = descriptor->u.Interrupt.Affinity;
                                             params.FullySpecified.ShareVector = descriptor->ShareDisposition;

                                             //
                                             // Default state is low.
                                             //
                                             DeviceContext->InterruptContext.State = 0;
                                             DeviceContext->InterruptContext.DeviceContext = DeviceContext;

                                             return IoConnectInterruptEx(&amp;params);
                              }
               }

               return STATUS_SUCCESS;
}

NTSTATUS
EvtDeviceReleaseHardware(
               __in  WDFDEVICE Device,
               __in  WDFCMRESLIST ResourcesTranslated
)
{
               PDEVICE_CONTEXT DeviceContext = YourGetDeviceContext(Device);

               if (NULL != DeviceContext->Interrupt)
               {
                              IO_DISCONNECT_INTERRUPT_PARAMETERS params;

                              params.Version = CONNECT_FULLY_SPECIFIED;
                              params.ConnectionContext.InterruptObject = DeviceContext->Interrupt;

                              IoDisconnectInterruptEx(&amp;params);
               }

               return STATUS_SUCCESS;
}
```

In the preceding code example, the driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function configures the device context and then calls [**IoInitializeDpcRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549307) to register a [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine.

The driver's [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine inverts the interrupt state value and then calls [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657) to queue the DPC.

In its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function, the driver initializes the state value to **FALSE** and then calls [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378). In its [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function, the driver calls [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093) to unregister its ISR.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Active-Both%20Interrupts%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




