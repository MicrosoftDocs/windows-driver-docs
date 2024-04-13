---
title: Reading and Filtering Debugging Messages
description: Reading and Filtering Debugging Messages
keywords: ["reading and filtering debugging messages", "debugging messages, reading and filtering"]
ms.date: 07/20/2020
---

# Reading and Filtering Debugging Messages

The [**DbgPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgprintex), [**vDbgPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-vdbgprintex), [**vDbgPrintExWithPrefix**](/windows-hardware/drivers/ddi/wdm/nf-wdm-vdbgprintexwithprefix), and [**KdPrintEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprintex) routines send a message to the kernel debugger under conditions that you specify. This procedure enables you to filter out low-priority messages.

> [!NOTE]
> In Microsoft Windows Server 2003 and earlier versions of Windows, the [**DbgPrint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgprint) and [**KdPrint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdprint) routines send messages to the kernel debugger unconditionally.
> In Windows Vista and later versions of Windows, these routines send messages conditionally, like **DbgPrintEx** and **KdPrintEx**.
> Whichever version of Windows you are using, you should use **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, and **KdPrintEx**, because these routines enable you to control the conditions under which the message is sent.

## To filter debugging messages

1. For each message that you want to send to the debugger, use **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, or **KdPrintEx** in your driver's code. Pass the appropriate component name to the *ComponentId* parameter, and pass a value to the *Level* parameter that reflects the severity or nature of this message. The message itself is passed to the *Format* and *arguments* parameters by using the same syntax as **printf**.

2. Set the value of the appropriate *component filter mask*. Each component has a different mask. The mask value indicates which of that component's messages are displayed. You can set the component filter mask in the registry by using a registry editor or in memory by using a kernel debugger.

3. Attach a kernel debugger to the computer. Every time that your driver passes a message to **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, or **KdPrintEx**, the values that are passed to *ComponentId* and *Level* are compared with the value of the corresponding component filter mask. If these values satisfy certain criteria, the message are sent to the kernel debugger and displayed. Otherwise, no message is sent.

> [!NOTE]
> All references on this page to **DbgPrintEx** apply equally to **KdPrintEx**, **vDbgPrintEx**, and **vDbgPrintExWithPrefix**.

## Identifying the Component Name

Each component has a separate filter mask. This allows the debugger to configure the filter for each component separately.

Each component is referred to in different ways, depending on the context. In the *ComponentId* parameter of **DbgPrintEx**, the component name is prefixed with "DPFLTR\_" and suffixed with "\_ID". In the registry, the component filter mask has the same name as the component itself. In the debugger, the component filter mask is prefixed with "Kd\_" and suffixed with "\_Mask".

There is a complete list of all component names (in DPFLTR\_*XXXX*\_ID format) in the Microsoft Windows Driver Kit (WDK) header dpfilter.h. Most of these component names are reserved for Windows and for drivers written by Microsoft.

There are six component names reserved for independent hardware vendors. To avoid mixing your driver's output with the output of Windows components, you should use one of the following component names:

| Component name | Driver type |
| --- | --- |
| IHVVIDEO | Video driver |
| IHVAUDIO | Audio driver |
| IHVNETWORK | Network driver |
| IHVSTREAMING | Kernel streaming driver |
| IHVBUS | Bus driver |
| IHVDRIVER | Any other type of driver |

For example, if you are writing a video driver, you would use DPFLTR\_IHVVIDEO\_ID as the *ComponentId* parameter of **DbgPrintEx**, use the value name **IHVVIDEO** in the registry, and refer to **Kd\_IHVVIDEO\_Mask** in the debugger.

All messages sent by **DbgPrint** and **KdPrint** are associated with the **DEFAULT** component.

### <span id="choosing_the_correct_level"></span><span id="CHOOSING_THE_CORRECT_LEVEL"></span>Choosing the Correct Level

The *Level* parameter of the **DbgPrintEx** routine is of type DWORD. It is used to determine the *importance bit field*. The connection between the *Level* parameter and this bit field depends on the size of *Level*:

- If *Level* is equal to a number between 0 and 31, inclusive, it is interpreted as a bit shift. The importance bit field is set to the value 1 &lt;&lt; *Level*. Thus choosing a value between 0 and 31 for *Level* results in a bit field with exactly one bit set. If *Level* is 0, the bit field is equivalent to 0x00000001;if *Level* is 31, the bit field is equivalent to 0x80000000.

- If *Level* is a number between 32 and 0xFFFFFFFF inclusive, the importance bit field is set to the value of *Level* itself.

Thus, if you wish to set the bit field to 0x00004000, you can specify *Level* as 0x00004000 or simply as 14. Note that certain bit field values are not possible by this system -- including a bit field which is entirely zero.

The following constants can be useful for setting the value of *Level*. They are defined in the Microsoft Windows Driver Kit (WDK) header dpfilter.h and the Windows SDK header ntrtl.h:

```cpp
#define   DPFLTR_ERROR_LEVEL     0
#define   DPFLTR_WARNING_LEVEL   1
#define   DPFLTR_TRACE_LEVEL     2
#define   DPFLTR_INFO_LEVEL      3
#define   DPFLTR_MASK   0x80000000
```

One easy way to use the *Level* parameter is to always use values between 0 and 31 -- using the bits 0, 1, 2, 3 with the meaning given by DPFLTR\_*XXXX*\_LEVEL, and using the other bits to mean whatever you choose.

Another easy way to use the *Level* parameter is to always use explicit bit fields. If you choose this method, you may wish to OR the value DPFLTR\_MASK with your bit field; this assures that you will not accidentally use a value less than 32.

To make your driver compatible with the way Windows uses message levels, you should only set the lowest bit (0x1) of the importance bit field if a serious error occurs. If you are using *Level* values less than 32, this corresponds to DPFLTR\_ERROR\_LEVEL. If this bit is set, your message is going to be viewed any time someone attaches a kernel debugger to a computer on which your driver is running.

The warning, trace, and information levels should be used in the appropriate situations. Other bits can be freely used for any purposes that you find useful. This allows you to have a wide variety of message types that can be selectively seen or hidden.

All messages sent by **DbgPrint** and **KdPrint** behave like **DbgPrintEx** and **KdPrintEx** messages with *Level* equal to DPFLTR\_INFO\_LEVEL. In other words, these messages have the third bit of their importance bit field set.

## Setting the Component Filter Mask

There are two ways to set a component filter mask:

- The component filter mask can be accessed in the registry key **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Debug Print Filter**. Using a registry editor, create or open this key. Under this key, create a value with the name of the desired component, in uppercase. Set it equal to the DWORD value that you wish to use as the component filter mask.

- If a kernel debugger is active, it can access the component filter mask value by dereferencing the address stored in the symbol **Kd\_**<em>XXXX</em>**\_Mask**, where *XXXX* is the desired component name. You can display the value of this mask in WinDbg or KD with the **dd (Display DWORD)** command, or enter a new component filter mask with the **ed (Enter DWORD)** command. If there is a danger of symbol ambiguity, you may wish to specify this symbol as **nt!Kd\_**<em>XXXX</em>**\_Mask**.

Filter masks stored in the registry take effect during boot. Filter masks created by the debugger take effect immediately, and persist until Windows is rebooted. A value set in the registry can be overridden by the debugger, but the component filter mask will return to the value specified in the registry if the system is rebooted.

There is also a system-wide mask called **WIN2000**. This is equal to 0x1 by default, though it can be changed through the registry or the debugger like all other components. When filtering is performed, each component filter mask is first ORed with the **WIN2000** mask. In particular, this means that components whose masks have never been specified default to 0x1.

## Criteria for Displaying the Message

When **DbgPrintEx** is called in kernel-mode code, Windows compares the message importance bit field specified by *Level* with the filter mask of the component specified by *ComponentId*.

> [!NOTE]
> Recall that when the *Level* parameter is between 0 and 31, the importance bitfield is equal to 1 << *Level*. But when the *Level* parameter is 32 or higher, the importance bitfield is simply equal to *Level*.

Windows performs an AND operation on the importance bit field and the component filter mask. If the result is nonzero, the message is sent to the debugger.

## Debug Filter Example

Suppose that before the last boot, you created the following values in the **Debug Print Filter** key:

- **IHVVIDEO**, with a value equal to DWORD 0x2

- **IHVBUS**, equal to DWORD 0x7FF

Now you issue the following commands in the kernel debugger:

```dbgcmd
kd> ed Kd_IHVVIDEO_Mask 0x8 
kd> ed Kd_IHVAUDIO_Mask 0x7 
```

At this point, the **IHVVIDEO** component has a filter mask of 0x8, the **IHVAUDIO** component has a filter mask of 0x7, and the **IHVBUS** component has a filter mask of 0x7FF.

However, because these masks are automatically ORed with the **WIN2000** system-wide mask (which is usually equal to 0x1), the **IHVVIDEO** mask is effectively equal to 0x9. Indeed, components whose filter masks have not been set at all (for instance, **IHVSTREAMING** or **DEFAULT**) will have a filter mask of 0x1.

Now suppose that the following function calls occur in various drivers:

```cpp
DbgPrintEx( DPFLTR_IHVVIDEO_ID,  DPFLTR_INFO_LEVEL,   "First message.\n");
DbgPrintEx( DPFLTR_IHVAUDIO_ID,  7,                   "Second message.\n");
DbgPrintEx( DPFLTR_IHVBUS_ID,    DPFLTR_MASK | 0x10,  "Third message.\n");
DbgPrint( "Fourth message.\n");
```

The first message has its *Level* parameter equal to DPFLTR\_INFO\_LEVEL, which is 3. Since this is less than 32, it is treated as a bit shift, resulting in an importance bit field of 0x8. This value is then ANDed with the effective **IHVVIDEO** component filter mask of 0x9, giving a nonzero result. So the first message is transmitted to the debugger.

The second message has its *Level* parameter equal to 7. Again, this is treated as a bit shift, resulting in an importance bit field of 0x80. This is then ANDed with the **IHVAUDIO** component filter mask of 0x7, giving a result of zero. So the second message is not transmitted.

The third message has its *Level* parameter equal to DPFLTR\_MASK | 0x10. This is greater than 31, and therefore the importance bit field is set equal to the value of *Level* -- in other words, to 0x80000010. This is then ANDed with the **IHVBUS** component filter mask of 0x7FF, giving a nonzero result. So the third message is transmitted to the debugger.

The fourth message was passed to **DbgPrint** instead of **DbgPrintEx**. In Windows Server 2003 and earlier versions of Windows, messages passed to this routine are always transmitted. In Windows Vista and later versions of Windows, messages passed to this routine are always given a default filter. The importance bit field is equal to 1 &lt;&lt; DPFLTR\_INFO\_LEVEL, which is 0x00000008. The component for this routine is **DEFAULT**. Since you have not set the **DEFAULT** component filter mask, it has a value of 0x1. When this is ANDed with the importance bit field, the result is zero. So the fourth message is not transmitted.

## DbgPrint buffer and the debugger

When the **DbgPrint**, **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, **KdPrint**, or **KdPrintEx** routine transmits a message to the debugger, the formatted string is sent to the **DbgPrint** buffer. The contents of this buffer are displayed immediately in the Debugger Command window, unless you disabled this display by using the **Buffer DbgPrint Output** option of GFlags.

During local kernel debugging, and any other time this display has been disabled, the contents of the DbgPrint buffer can only be viewed by using the [**!dbgprint**](../debuggercmds/-dbgprint.md) extension command.

Any single call to **DbgPrint**, **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, **KdPrint**, or **KdPrintEx** transmits only 512 bytes of information. Any output longer than the 512 bytes is lost. The DbgPrint buffer itself can hold up to 4 KB of data on a free build of Windows, and up to 32 KB of data on a checked build of Windows. On Windows Server 2003 and later versions of Windows, you can use the KDbgCtrl tool to alter the size of the DbgPrint buffer. This tool is part of Debugging Tools for Windows.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

If a message is filtered out because of its *ComponentId* and *Level* values, it is not transmitted across the debugging connection. Therefore there is no way to display this message in the debugger.
