---
title: Command Execution Order
author: windows-driver-content
description: Command Execution Order
ms.assetid: 2bf7438c-bfb0-407f-9c80-be3b8a9322f9
keywords: ["printer commands WDK Unidrv , execution order", "sequence numbers WDK Unidrv"]
---

# Command Execution Order


## <a href="" id="ddk-command-execution-order-gg"></a>


Printer commands must be sent to printer hardware in a meaningful order. For most of the command names defined in the GPD language, Unidrv knows when to send the command's escape sequence to the printer. There are two exceptions:

The [option selection command](option-selection-command.md)

[Printer configuration commands](printer-configuration-commands.md)

For both of these command types, you must specify the order in which the commands should be executed.

Command execution order is made up of two components -- a job section name and a sequence order number. The Unidrv driver divides each print job into six sections. For each section, Unidrv sends the printer the commands assigned to the section, in the specified sequence. The following sections are defined:

<a href="" id="job-setup"></a>JOB\_SETUP  
Commands assigned to the JOB\_SETUP section are sent once per job. They are the first commands sent when a new job begins. These commands are sent from within Unidrv's implementation of the [**DrvStartDoc**](https://msdn.microsoft.com/library/windows/hardware/ff556296) function.

<a href="" id="doc-setup"></a>DOC\_SETUP  
Commands assigned to the DOC\_SETUP section are sent before the first page of a document is sent. The commands are sent from within Unidrv's implementation of the DrvStartDoc function. (These commands are also sent after an application calls the Win32 ResetDC function. Commands in this section must not remove downloaded information, such as soft fonts and patterns.)

<a href="" id="page-setup"></a>PAGE\_SETUP  
Commands assigned to the PAGE\_SETUP section are sent at the beginning of each new page, before drawing begins. These commands are sent from within Unidrv's implementation of the [**DrvStartPage**](https://msdn.microsoft.com/library/windows/hardware/ff556298) function.

<a href="" id="page-finish"></a>PAGE\_FINISH  
Commands assigned to the PAGE\_FINISH section are sent at the end of each page, after drawing is complete. These commands are sent from within Unidrv's implementation of the [*DrvSendPage*](https://msdn.microsoft.com/library/windows/hardware/ff556281) function.

<a href="" id="doc-finish"></a>DOC\_FINISH  
Commands assigned to the DOC\_FINISH section are sent after the last page of a document is sent. The commands are sent from within Unidrv's implementation of the [**DrvEndDoc**](https://msdn.microsoft.com/library/windows/hardware/ff556215) function. (Commands in this section must not remove downloaded information, such as soft fonts and patterns.)

<a href="" id="job-finish"></a>JOB\_FINISH  
Commands assigned to the JOB\_FINISH section are sent once per job. They are the last commands sent when a job ends. These commands are sent from within Unidrv's implementation of the DrvEndDoc function.

Within each of these sections, commands are executed in the order indicated by their sequence numbers.

To specify a command's section and sequence number, use the **\*Order** attribute, which is described in [Command Attributes](command-attributes.md). The format is:

**\*Order**: *SectionName*.*SequenceNumber*

where *SectionName* is one of JOB\_SETUP, DOC\_SETUP, PAGE\_SETUP, PAGE\_FINISH, DOC\_FINISH, or JOB\_FINISH, and *SequenceNumber* is a numeric value.

Sequence numbers do not have to be consecutive, but each number specified within a section must be unique. Commands within a section are executed from the one with the lowest sequence number to that with the highest. For example, the following entries indicate that options for the **InputBin**, **PaperSize**, and **Resolution** features are assigned to the DOC\_SETUP section and are sent in the specified order:

```
*Feature: InputBin
{
    *Option: Auto
    {
        *Name: "Auto Tray"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.50
            *Cmd: "<1B>(1<010014>"
        }
    }
    ...
}
*Feature: PaperSize
{
    *DefaultOption: Letter
    *Option: Letter
    {
        *Name: "Letter size"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.60
            *Cmd: "<1B>(g<0300>n<01>r"
        }
    }
    ...
}
*Feature: Resolution
{
    *DefaultOption: 360dpi
    *Option: 360dpi
    {
        *Name: "360 dpi x 360dpi"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.70
            *Cmd: "<1B>(d<020001>"
        }
    }
    ...
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Command%20Execution%20Order%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


