---
title: Reading and Filtering Debugging Messages
description: Reading and Filtering Debugging Messages
ms.assetid: 785469d2-30b8-4f73-b397-80bf89ed20ea
keywords: ["reading and filtering debugging messages", "debugging messages, reading and filtering"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Reading and Filtering Debugging Messages


## <span id="ddk_reading_and_filtering_debugging_messages_dbg"></span><span id="DDK_READING_AND_FILTERING_DEBUGGING_MESSAGES_DBG"></span>


Kernel-mode code can use the **DbgPrintEx** and **KdPrintEx** routines to send a messages to the kernel debugger that are only transmitted under certain conditions. This allows you to filter out messages that you are not interested in.

**Note**   In Windows Server 2003 and earlier versions of Windows, **DbgPrint** and **KdPrint** send messages to the kernel debugger unconditionally. In Windows Vista and later versions of Windows, these routines send messages conditionally, like **DbgPrintEx** and **KdPrintEx**. Whichever version of Windows you are using, it is recommended that you use **DbgPrintEx** and **KdPrintEx**, since these allow you to control the conditions under which the message will be sent.

 

For complete documentation of these routines, see the Windows Driver Kit.

The basic procedure is as follows:

**To filter debugging messages**

1.  For each message you wish to send to the debugger, use the function **DbgPrintEx** or **KdPrintEx** in your driver's code. Pass the appropriate component name to the *ComponentId* parameter, and pass a value to the *Level* parameter that reflects the severity or nature of this message. The message itself is passed to the *Format* and *arguments* parameters as with **printf**.

2.  Set the value of the appropriate *component filter mask*. Each component has a different mask; the mask value indicates which of that component's messages will be displayed. The component filter mask may be set in the registry using a registry editor, or in memory using a kernel debugger.

3.  Attach a kernel debugger to the computer. Each time your driver passes a message to **DbgPrintEx** or **KdPrintEx**, the values passed to *ComponentId* and *Level* will be compared with the value of the corresponding component filter mask. If these values satisfy certain criteria, the message will be sent to the kernel debugger and displayed. Otherwise, no message will be sent.

Full details follow. All references on this page to **DbgPrintEx** apply equally to **KdPrintEx**.

### <span id="identifying-the-component-name"></span><span id="IDENTIFYING_THE_COMPONENT_NAME"></span>Identifying the Component Name

Each component has a separate filter mask. This allows the debugger to configure the filter for each component separately.

Each component is referred to in different ways, depending on the context. In the *ComponentId* parameter of **DbgPrintEx**, the component name is prefixed with "DPFLTR\_" and suffixed with "\_ID". In the registry, the component filter mask has the same name as the component itself. In the debugger, the component filter mask is prefixed with "Kd\_" and suffixed with "\_Mask".

There is a complete list of all component names (in DPFLTR\_*XXXX*\_ID format) in the Microsoft Windows Driver Kit (WDK) header ntddk.h and the Windows SDK header ntrtl.h. Most of these component names are reserved for Windows and for drivers written by Microsoft.

There are six component names reserved for independent hardware vendors. To avoid mixing your driver's output with the output of Windows components, you should use one of the following component names:

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
<td align="left"><p><strong>IHVVIDEO</strong></p></td>
<td align="left"><p>Video driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IHVAUDIO</strong></p></td>
<td align="left"><p>Audio driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IHVNETWORK</strong></p></td>
<td align="left"><p>Network driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IHVSTREAMING</strong></p></td>
<td align="left"><p>Kernel streaming driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IHVBUS</strong></p></td>
<td align="left"><p>Bus driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IHVDRIVER</strong></p></td>
<td align="left"><p>Any other type of driver</p></td>
</tr>
</tbody>
</table>

 

For example, if you are writing a video driver, you would use DPFLTR\_IHVVIDEO\_ID as the *ComponentId* parameter of **DbgPrintEx**, use the value name **IHVVIDEO** in the registry, and refer to **Kd\_IHVVIDEO\_Mask** in the debugger.

In Windows Vista and later versions of Windows, all messages sent by **DbgPrint** and **KdPrint** are associated with the **DEFAULT** component.

### <span id="choosing_the_correct_level"></span><span id="CHOOSING_THE_CORRECT_LEVEL"></span>Choosing the Correct Level

The *Level* parameter of the **DbgPrintEx** routine is of type DWORD. It is used to determine the *importance bit field*. The connection between the *Level* parameter and this bit field depends on the size of *Level*:

-   If *Level* is equal to a number between 0 and 31, inclusive, it is interpreted as a bit shift. The importance bit field is set to the value 1 &lt;&lt; *Level*. Thus choosing a value between 0 and 31 for *Level* results in a bit field with exactly one bit set. If *Level* is 0, the bit field is equivalent to 0x00000001;if *Level* is 31, the bit field is equivalent to 0x80000000.

-   If *Level* is a number between 32 and 0xFFFFFFFF inclusive, the importance bit field is set to the value of *Level* itself.

Thus, if you wish to set the bit field to 0x00004000, you can specify *Level* as 0x00004000 or simply as 14. Note that certain bit field values are not possible by this system -- including a bit field which is entirely zero.

The following constants can be useful for setting the value of *Level*. They are defined in the Microsoft Windows Driver Kit (WDK) header ntddk.h and the Windows SDK header ntrtl.h:

```cpp
#define   DPFLTR_ERROR_LEVEL     0
#define   DPFLTR_WARNING_LEVEL   1
#define   DPFLTR_TRACE_LEVEL     2
#define   DPFLTR_INFO_LEVEL      3
#define   DPFLTR_MASK    0x8000000
```

One easy way to use the *Level* parameter is to always use values between 0 and 31 -- using the bits 0, 1, 2, 3 with the meaning given by DPFLTR\_*XXXX*\_LEVEL, and using the other bits to mean whatever you choose.

Another easy way to use the *Level* parameter is to always use explicit bit fields. If you choose this method, you may wish to OR the value DPFLTR\_MASK with your bit field; this assures that you will not accidentally use a value less than 32.

To make your driver compatible with the way Windows uses message levels, you should only set the lowest bit (0x1) of the importance bit field if a serious error occurs. If you are using *Level* values less than 32, this corresponds to DPFLTR\_ERROR\_LEVEL. If this bit is set, your message is going to be viewed any time someone attaches a kernel debugger to a computer on which your driver is running.

The warning, trace, and information levels should be used in the appropriate situations. Other bits can be freely used for any purposes that you find useful. This allows you to have a wide variety of message types that can be selectively seen or hidden.

In Windows Vista and later versions of Windows, all messages sent by **DbgPrint** and **KdPrint** behave like **DbgPrintEx** and **KdPrintEx** messages with *Level* equal to DPFLTR\_INFO\_LEVEL. In other words, these messages have the third bit of their importance bit field set.

### <span id="setting-the-component-filter-mask"></span><span id="SETTING_THE_COMPONENT_FILTER_MASK"></span>Setting the Component Filter Mask

There are two ways to set a component filter mask:

- The component filter mask can be accessed in the registry key **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Debug Print Filter**. Using a registry editor, create or open this key. Under this key, create a value with the name of the desired component, in uppercase. Set it equal to the DWORD value that you wish to use as the component filter mask.

- If a kernel debugger is active, it can access the component filter mask value by dereferencing the address stored in the symbol **Kd\_**<em>XXXX</em>**\_Mask**, where *XXXX* is the desired component name. You can display the value of this mask in WinDbg or KD with the **dd (Display DWORD)** command, or enter a new component filter mask with the **ed (Enter DWORD)** command. If there is a danger of symbol ambiguity, you may wish to specify this symbol as **nt!Kd\_**<em>XXXX</em>**\_Mask**.

Filter masks stored in the registry take effect during boot. Filter masks created by the debugger take effect immediately, and persist until Windows is rebooted. A value set in the registry can be overridden by the debugger, but the component filter mask will return to the value specified in the registry if the system is rebooted.

There is also a system-wide mask called **WIN2000**. This is equal to 0x1 by default, though it can be changed through the registry or the debugger like all other components. When filtering is performed, each component filter mask is first ORed with the **WIN2000** mask. In particular, this means that components whose masks have never been specified default to 0x1.

### <span id="criteria-for-displaying_the_message"></span><span id="CRITERIA_FOR_DISPLAYING_THE_MESSAGE"></span>Criteria for Displaying the Message

When **DbgPrintEx** is called in kernel-mode code, Windows compares the message importance bit field specified by *Level* with the filter mask of the component specified by *ComponentId*.

**Note**   Recall that when the *Level* parameter is between 0 and 31, the importance bit field is equal to 1 &lt;&lt; *Level*, but when the *Level* parameter is 32 or higher, the importance bit field is simply equal to *Level*.

 

Windows performs an AND operation on the importance bit field and the component filter mask. If the result is nonzero, the message is sent to the debugger.

### <span id="example"></span><span id="EXAMPLE"></span>Example

Here is an example.

Suppose that before the last boot, you created the following values in the **Debug Print Filter** key:

-   **IHVVIDEO**, with a value equal to DWORD 0x2

-   **IHVBUS**, equal to DWORD 0x7FF

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

### <span id="the-dbgprint-buffer"></span><span id="THE_DBGPRINT_BUFFER"></span>The DbgPrint Buffer

When **DbgPrint**, **DbgPrintEx**, **KdPrint**, or **KdPrintEx** transmits a message to the debugger, the formatted string is sent to the *DbgPrint buffer*. In most cases, the contents of this buffer are displayed immediately in the Debugger Command window. This display can be disabled by using the **Buffer DbgPrint Output** option of the Global Flags Utility (gflags.exe). This display does not automatically appear during local kernel debugging.

During local kernel debugging, and any other time this display has been disabled, the contents of the DbgPrint buffer can only be viewed by using the [**!dbgprint**](-dbgprint.md) extension command.

Any single call to **DbgPrint**, **DbgPrintEx**, **KdPrint**, or **KdPrintEx** will only transmit 512 bytes of information. Any output longer than this will be lost. The DbgPrint buffer itself can hold up to 4 KB of data on a free build of Windows, and up to 32 KB of data on a checked build of Windows. On Windows Server 2003 and later versions of Windows, you can use the KDbgCtrl tool to alter the size of the DbgPrint buffer. See [Using KDbgCtrl](using-kdbgctrl.md) for details.

If a message is filtered out because of its *ComponentId* and *Level* values, it is not transmitted across the debugging connection. Therefore there is no way to display this message in the debugger.

 

 





