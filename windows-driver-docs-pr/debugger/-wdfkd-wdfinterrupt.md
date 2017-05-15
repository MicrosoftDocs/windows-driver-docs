---
title: wdfkd.wdfinterrupt
description: The wdfkd.wdfinterrupt extension displays information about a WDFINTERRUPT object.
ms.assetid: 3e032095-94fe-41d5-aeed-645d6b544105
keywords: ["wdfkd.wdfinterrupt Windows Debugging"]
topic_type:
- apiref
api_name:
- wdfkd.wdfinterrupt
api_type:
- NA
---

# !wdfkd.wdfinterrupt


The **!wdfkd.wdfinterrupt** extension displays information about a WDFINTERRUPT object.

``` syntax
!wdfkd.wdfinterrupt Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFINTERRUPT object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays the interrupt service routines (ISRs) for the interrupt dispatch table (IDT) associated with this WDFINTERRUPT object. Setting this flag is equivalent to following the **!wdfinterrupt** extension with the [**!idt**](-idt.md) extension.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The following example shows the output of the **!wdfinterrupt** extension with bit 0 set in the *Flags* parameter (so the output displays information about the IDT).

```
kd> !wdfkd.wdfinterrupt 0x7a988698  1 

# Dumping WDFINTERRUPT 0x7a988698
=========================
  Interrupt Type: Line-based, Connected, Enabled
  Vector: 0xa1 (!idt 0xa1)
  Irql: 0x9
  Mode: LevelSensitive
  Polarity: WdfInterruptPolarityUnknown
  ShareDisposition: CmResourceShareShared
  FloatingSave: FALSE
  Interrupt Priority Policy: WdfIrqPriorityUndefined
  Processor Affinity Policy: WdfIrqPolicyOneCloseProcessor
  Processor Group: 0
  Processor Affinity: 0x3

  dt nt!KINTERRUPT 0x8594eb28

  EvtInterruptIsr: 1394ohci!Interrupt::WdfEvtInterruptIsr (0x8d580552)
  EvtInterruptDpc: 1394ohci!Interrupt::WdfEvtInterruptDpc (0x8d580682)

Dumping IDT:

a1:          85167a58 ndis!ndisMiniportIsr (KINTERRUPT 85167a00)
                                    Wdf01000!FxInterrupt::_InterruptThunk (KINTERRUPT 85987500)

To get ISR from KINTERRUPT: 
   dt <KINTERRUPT> nt!KINTERRUPT ServiceContext
   dt <ServiceContext> wdf01000!FxInterrupt m_EvtInterruptIsr
```

In the preceding example, the display concludes with two suggested [**dt (Display Type)**](dt--display-type-.md) commands that can be used to display additional data.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfinterrupt%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




