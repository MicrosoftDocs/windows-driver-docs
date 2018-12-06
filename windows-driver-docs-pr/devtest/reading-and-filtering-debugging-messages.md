---
title: Reading and Filtering Debugging Messages
description: Reading and Filtering Debugging Messages
ms.assetid: 2ad320f6-596d-4b4c-bfad-d570c856bcc7
keywords:
- debugging code WDK , reading messages
- debugging code WDK , filtering messages
- reading debugging messages
- filtering debugging messages WDK
- routines WDK debugging , message filtering
- filter masks WDK debugging
- component names WDK debugging
- importance bitfield WDK debugging
- levels WDK debugging
- Level parameter
- displaying debugging messages
- prioritizing debugging messages WDK
- DbgPrint buffer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading and Filtering Debugging Messages


## <span id="ddk_reading_and_filtering_debugging_messages_tools"></span><span id="DDK_READING_AND_FILTERING_DEBUGGING_MESSAGES_TOOLS"></span>


The [**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634), [**vDbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff556075), [**vDbgPrintExWithPrefix**](https://msdn.microsoft.com/library/windows/hardware/ff556076), and [**KdPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff548100) routines send a message to the kernel debugger under conditions that you specify. This procedure enables you to filter out low-priority messages.

**Note**   In Microsoft Windows Server 2003 and earlier versions of Windows, the [**DbgPrint**](https://msdn.microsoft.com/library/windows/hardware/ff543632) and [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092) routines send messages to the kernel debugger unconditionally. In Windows Vista and later versions of Windows, these routines send messages conditionally, like **DbgPrintEx** and **KdPrintEx**. Whichever version of Windows you are using, you should use **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, and **KdPrintEx**, because these routines enable you to control the conditions under which the message is sent.

 

**To filter debugging messages**

1.  For each message that you want to send to the debugger, use **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, or **KdPrintEx** in your driver's code. Pass the appropriate component name to the *ComponentId* parameter, and pass a value to the *Level* parameter that reflects the severity or nature of this message. The message itself is passed to the *Format* and *arguments* parameters by using the same syntax as **printf**.

2.  Set the value of the appropriate *component filter mask*. Each component has a different mask. The mask value indicates which of that component's messages are displayed. You can set the component filter mask in the registry by using a registry editor or in memory by using a kernel debugger.

3.  Attach a kernel debugger to the computer. Every time that your driver passes a message to **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, or **KdPrintEx**, the values that are passed to *ComponentId* and *Level* are compared with the value of the corresponding component filter mask. If these values satisfy certain criteria, the message are sent to the kernel debugger and displayed. Otherwise, no message is sent.

For a full explanation, see the following section.

**Note**   All references on this page to **DbgPrintEx** apply equally to **KdPrintEx**, **vDbgPrintEx**, and **vDbgPrintExWithPrefix**.

 

-   [Identifying the Component Name](#identifying-the-component-name)
-   [Choosing the Correct Level](#choosing-the-correct-level)
-   [Setting the Component Filter Mask](#setting-the-component-filter-mask)
-   [Criteria for Displaying the Message](#criteria-for-displaying-the-message)
-   [Example](#example)
-   [DbgPrint Buffer and the Debugger](#dbgprint-buffer-and-the-debugger)

### Identifying the Component Name

Each component has a separate filter mask. This mask enables the debugger to configure the filter for each component separately.

Each component is referred to in different ways, depending on the context. In the *ComponentId* parameter of **DbgPrintEx**, the component name is prefixed with "DPFLTR\_" and suffixed with "\_ID". In the registry, the component filter mask has the same name as the component itself. In the debugger, the component filter mask is prefixed with "Kd\_" and suffixed with "\_Mask".

There is a complete list of component names (in DPFLTR\_*XXXX*\_ID format) in the Dpfilter.h header file in the Windows Driver Kit (WDK). Most of these component names are reserved for Windows and for drivers that are written by Microsoft.

There are six component names that are reserved for independent hardware vendors. To avoid mixing your driver's output with the output of Windows components, you should use one of the following component names.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Component name</th>
<th align="left">Driver type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IHVVIDEO</p></td>
<td align="left"><p>Video driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>IHVAUDIO</p></td>
<td align="left"><p>Audio driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IHVNETWORK</p></td>
<td align="left"><p>Network driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>IHVSTREAMING</p></td>
<td align="left"><p>Kernel streaming driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IHVBUS</p></td>
<td align="left"><p>Bus driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>IHVDRIVER</p></td>
<td align="left"><p>Any other type of driver</p></td>
</tr>
</tbody>
</table>

 

For example, if you are writing a video driver, you would use DPFLTR\_IHVVIDEO\_ID as the *ComponentId* parameter of **DbgPrintEx**, use the value name IHVVIDEO in the registry, and refer to **Kd\_IHVVIDEO\_Mask** in the debugger.

In Windows Vista and later versions of Windows, all messages that **DbgPrint** and **KdPrint** send are associated with the DEFAULT component (DPFLTR\_DEFAULT\_ID).

### Choosing the Correct Level

The *Level* parameter of the **DbgPrintEx** routine is of type DWORD. It is used to determine the *importance bitfield*. The connection between the *Level* parameter and this bitfield depends on the size of *Level*:

-   If *Level* is equal to a number between 0 and 31, inclusive, the importance bitfield is interpreted as a bit shift. The importance bitfield is set to the value 1 &lt;&lt; *Level*. Thus, if you choose a value between 0 and 31 for *Level*, the bitfield has exactly one bit set. If *Level* is 0, the bitfield is equivalent to 0x00000001. If *Level* is 31, the bitfield is equivalent to 0x80000000.

-   If *Level* is a number between 32 and 0xFFFFFFFF inclusive, the importance bitfield is set to the value of *Level* itself.

Thus, if you want to set the bitfield to 0x00004000, you can specify *Level* as 0x00004000 or simply as 14. As a consequence of this system, some bitfield values cannot be produced--including a bitfield that is entirely zero.

The following constants can be useful for setting the value of *Level*. They are defined in the Dpfilter.h WDK header file:

```ManagedCPlusPlus
#define DPFLTR_ERROR_LEVEL 0
#define DPFLTR_WARNING_LEVEL 1
#define DPFLTR_TRACE_LEVEL 2
#define DPFLTR_INFO_LEVEL 3
#define DPFLTR_MASK 0x80000000
```

One easy way to use the *Level* parameter is to always use values between 0 and 31--using the bits 0, 1, 2, and 3 with the meaning given by DPFLTR\_*XXXX*\_LEVEL, and using the other bits to mean whatever you choose.

Another easy way to use the *Level* parameter is to always use explicit bitfields. If you choose this method, you may wish to use a bitwise OR of the value DPFLTR\_MASK with your bitfield. This value ensures that you do not accidentally use a value less than 32.

To make your driver compatible with the way that Windows uses message levels, you should set only the lowest bit (0x1) of the importance bitfield if a serious error occurs. If you are using *Level* values less than 32, this value corresponds to DPFLTR\_ERROR\_LEVEL. If the importance bitfield is set, your message will be viewed any time that someone attaches a kernel debugger to a computer on which your driver is running.

Use the warning, trace, and information levels in the appropriate situations. You can use other bits for any purposes that you find useful. This ability enables you to have a wide variety of message types that can be selectively seen or hidden.

In Windows Vista and later versions of Windows, all messages sent by **DbgPrint** and **KdPrint** behave like **DbgPrintEx** and **KdPrintEx** messages with *Level* equal to DPFLTR\_INFO\_LEVEL. In other words, these messages have the third bit of their importance bitfield set.

### Setting the Component Filter Mask

There are two ways to set a component filter mask:

- On the target computer, you can access the component filter mask in the registry key **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Debug Print Filter**. Using a registry editor, create or open this key. Under this key, create a value with the name of the desired component, in uppercase letters (for example, **DEFAULT** or **IHVDRIVER**). Set this value equal to the DWORD value that you want to use as the component filter mask (for example, 0x8 to display DPFLTR\_INFO\_LEVEL messages, in addition to DPFLTR\_ERROR\_LEVEL, or set the mask to 0xF to display all messages).

- If a kernel debugger is active, it can access the component filter mask value by dereferencing the address that is stored in the symbol **Kd\_**<em>XXXX</em>**\_Mask**, where *XXXX* is the desired component name. You can display the value of this mask in WinDbg or KD with the **dd (Display DWORD)** command, or enter a new component filter mask with the **ed (Enter DWORD)** command. If there is a danger of symbol ambiguity, you might want to specify this symbol as **nt!Kd\_**<em>XXXX</em>**\_Mask**.

Filter masks that are stored in the registry take effect during boot. Filter masks that are created by the debugger take effect immediately and persist until the target computer is restarted. The debugger can override a value that is set in the registry, but the component filter mask returns to the value that is specified in the registry if the target computer is restarted.

There is also a system-wide mask called WIN2000. By default, this mask is equal to 0x1, but you can change it through the registry or the debugger like all other components. When filtering is performed, each component filter mask is first combined with the WIN2000 mask by using a bitwise OR. In particular, this combination means that components whose masks have never been specified default to 0x1.

### Criteria for Displaying the Message

When **DbgPrintEx** is called in kernel-mode code, Windows compares the message importance bitfield that is specified by *Level* with the filter mask of the component that is specified by *ComponentId*.

**Note**   Recall that when the *Level* parameter is between 0 and 31, the importance bitfield is equal to 1 &lt;&lt; *Level*. But when the *Level* parameter is 32 or higher, the importance bitfield is simply equal to *Level*.

 

Windows performs an AND operation on the importance bitfield and the component filter mask. If the result is nonzero, the message is sent to the debugger.

### Example

Suppose that before the last boot, you created the following values in the **Debug Print Filter** key:

-   IHVVIDEO, with a value equal to DWORD 0x2.

-   IHVBUS, equal to DWORD 0x7FF.

Now you issue the following commands in the kernel debugger:

```
kd> ed Kd_IHVVIDEO_Mask 0x8 
kd> ed Kd_IHVAUDIO_Mask 0x7 
```

At this point, the IHVVIDEO component has a filter mask of 0x8, the IHVAUDIO component has a filter mask of 0x7, and the IHVBUS component has a filter mask of 0x7FF.

However, because these masks are automatically combined with the WIN2000 system-wide mask (which is usually equal to 0x1) by using a bitwise OR, the IHVVIDEO mask is effectively equal to 0x9. Components whose filter masks have not been set at all (for instance, IHVSTREAMING or DEFAULT) have a filter mask of 0x1.

Now suppose that the following function calls occur in various drivers:

```
DbgPrintEx( DPFLTR_IHVVIDEO_ID,  DPFLTR_INFO_LEVEL,   "First message.\n");
DbgPrintEx( DPFLTR_IHVAUDIO_ID,  7,                   "Second message.\n");
DbgPrintEx( DPFLTR_IHVBUS_ID,    DPFLTR_MASK | 0x10,  "Third message.\n");
DbgPrint( "Fourth message.\n");
```

The first message has its *Level* parameter equal to DPFLTR\_INFO\_LEVEL, which is 3. Because this value is less than 32, it is treated as a bit shift, resulting in an importance bitfield of 0x8. This value is then combined with the effective IHVVIDEO component filter mask of 0x9 by using an AND operation, giving a nonzero result. So the first message is transmitted to the debugger.

The second message has its *Level* parameter equal to 7. Again, this value is treated as a bit shift, resulting in an importance bitfield of 0x80. This value is then combined with the IHVAUDIO component filter mask of 0x7 by using an AND operation, giving a result of zero. So the second message is not transmitted.

The third message has its *Level* parameter equal to DPFLTR\_MASK | 0x10. This value is greater than 31, and therefore the importance bitfield is set equal to the value of *Level*--in other words, to 0x80000010. This value is then combined with the IHVBUS component filter mask of 0x7FF by using an AND operation, giving a nonzero result. So the third message is transmitted to the debugger.

The fourth message was passed to the **DbgPrint** routine instead of the **DbgPrintEx** routine. In Windows Server 2003 and earlier versions of Windows, messages that are passed to **DbgPrint** are always transmitted. In Windows Vista and later versions of Windows, messages that are passed to **DbgPrint** are always given a default filter. The importance bitfield is equal to 1 &lt;&lt; DPFLTR\_INFO\_LEVEL, which is 0x00000008. The component for this routine is DEFAULT. Because you have not set the DEFAULT component filter mask, it has a value of 0x1. When this mask is combined with the importance bitfield by using an AND operation, the result is zero. So the fourth message is not transmitted.

### DbgPrint Buffer and the Debugger

When the **DbgPrint**, **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, **KdPrint**, or **KdPrintEx** routine transmits a message to the debugger, the formatted string is sent to the **DbgPrint** buffer. The contents of this buffer are displayed immediately in the Debugger Command window, unless you disabled this display by using the **Buffer DbgPrint Output** option of GFlags.

If you disabled this display, you can view the contents of the DbgPrint buffer only by using the **!dbgprint** extension command. For information about debugger extensions, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

Any single call to **DbgPrint**, **DbgPrintEx**, **vDbgPrintEx**, **vDbgPrintExWithPrefix**, **KdPrint**, or **KdPrintEx** transmits only 512 bytes of information. Any output longer than the 512 bytes is lost. The DbgPrint buffer itself can hold up to 4 KB of data on a free build of Windows, and up to 32 KB of data on a checked build of Windows. On Windows Server 2003 and later versions of Windows, you can use the KDbgCtrl tool to alter the size of the DbgPrint buffer. This tool is part of Debugging Tools for Windows.

If a message is filtered out because of its *ComponentId* and *Level* values, it is not transmitted across the debugging connection. Therefore, there is no way to display this message in the debugger.

 

 





