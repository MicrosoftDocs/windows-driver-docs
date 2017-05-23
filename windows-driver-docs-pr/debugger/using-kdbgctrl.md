---
title: Using KDbgCtrl
description: Using KDbgCtrl
ms.assetid: 386e8861-dd55-440c-9309-7e8cf6c27690
keywords: ["KDbgCtrl", "KDbgCtrl, basic use", "DbgPrint buffer, changing buffer size", "DbgPrint buffer, KDbgCtrl utility"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using KDbgCtrl


The KDbgCtrl (Kernel Debugging Control, kdbgctrl.exe) tool can be used to control the kernel debugging connection from the target computer.

To use this tool, your target computer must be running Windows Server 2003 or a later version of Windows.

KDbgCtrl can control five different settings: Full Kernel Debugging, Automatic Kernel Debugging, User-Mode Error Handling, Blocking of Kernel Debugging, and the size of the DbgPrint buffer.

To use KDbgCtrl, you must have already enabled kernel debugging in the boot settings of the target computer before the last boot. KDbgCtrl cannot be used to enable kernel debugging if this was not done. See [Boot Parameters to Enable Debugging](https://msdn.microsoft.com/library/windows/hardware/ff542279) for details on these boot settings.

### <span id="full_kernel_debugging"></span><span id="FULL_KERNEL_DEBUGGING"></span>Full Kernel Debugging

When Full Kernel Debugging is enabled, a kernel debugger running on the host computer can break into the target computer. The target computer will break into the kernel debugger if a kernel-mode exception is hit. Messages from the target to the host, such as **DbgPrint** output, symbol load messages, and redirected user-mode debuggers, are also allowed.

If this setting is disabled, all signals from the host computer will be ignored by the target.

Full Kernel Debugging is enabled by default. To check the current setting value, use **kdbgctrl -c**. To disable this setting, use **kdbgctrl -d**. To enable this setting, use **kdbgctrl -e**.

If you wish to check the current setting and use it to control execution within a batch file, you can use the **kdbgctrl -cx** command. For details on this command, see [**KDbgCtrl Command-Line Options**](kdbgctrl-command-line-options.md).

### <span id="automatic_kernel_debugging"></span><span id="AUTOMATIC_KERNEL_DEBUGGING"></span>Automatic Kernel Debugging

If Full Kernel Debugging is enabled, the current setting for Automatic Kernel Debugging is immaterial -- all communication is permitted.

When Full Kernel Debugging is disabled and Automatic Kernel Debugging is enabled, only the target computer can initiate a debugging connection.

In this case, only a kernel-mode exception, breakpoint, or other kernel-mode event will cause a connection to be established. The connection will not be established for **DbgPrint** output, symbol load messages, redirected user-mode debugger input and output, or other similar messages -- these will be stored in the DbgPrint buffer instead of being sent to the kernel debugger.

If an exception or event causes the target to break into the kernel debugger, then Full Kernel Debugging will be automatically turned on, just as if you had executed **kdbgctrl -e**.

Automatic Kernel Debugging is disabled by default (although this is immaterial unless Full Kernel Debugging is disabled as well). To check the current setting value, use **kdbgctrl -ca**. To disable this setting, use **kdbgctrl -da**. To enable this setting, use **kdbgctrl -ea**.

### <span id="user_mode_error_handling"></span><span id="USER_MODE_ERROR_HANDLING"></span>User-Mode Error Handling

When User-Mode Error Handling is enabled, some user-mode events will cause the target computer to break into the kernel debugger.

Specifically, all **int 3** interrupts -- such as breakpoints inserted into the code by a debugger or calls to **DbgBreakPoint** -- will cause a break into the kernel debugger. However, standard exceptions -- such as access violations and division by zero -- will usually not be sent to the kernel debugger.

If a user-mode debugger is already attached to the process, this debugger will capture all user-mode errors, and the kernel debugger will not be alterted. For the precedence ranking of the various user-mode error handlers, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

For User-Mode Error Handling to function, either Full Kernel Debugging or Automatic Kernel Debugging must be enabled as well.

User-Mode Error Handling is enabled by default. To check the current setting value, use **kdbgctrl -cu**. To disable this setting, use **kdbgctrl -du**. To enable this setting, use **kdbgctrl -eu**.

### <span id="blocking_kernel_debugging"></span><span id="BLOCKING_KERNEL_DEBUGGING"></span>Blocking Kernel Debugging

In some cases you might want to set up the target computer for kernel debugging, but wait to enable kernel debugging until after the target computer is started. You can do that by blocking kernel debugging.

To block kernel debugging, set up the target computer by using commands similar to the following:

``` syntax
bcdedit /debug on
bcdedit /dbgsettings 1394 channel:32 /start DISABLE /noumex
```

When you restart the target computer, it will be prepared for kernel debugging, but kernel debugging and User-Mode Error Handling will be disabled. At that point, a host computer will not be able to attach to the target computer, bug checks will not be caught by the kernel debugger, and user-mode exceptions will not cause a break in to the kernel debugger.

When you are ready, you can enable kernel debugging (without restarting the target computer) by entering the following commands.

``` syntax
kdbgctrl -db
kdbgctrl -e
```

Later, you can disable kernel debugging by entering the following commands.

``` syntax
kdbgctrl -d
kdbgctrl -eb
```

You can use **kdbgctrl -cb** to check whether kernel debugging is blocked.

### <span id="the_dbgprint_buffer_size"></span><span id="THE_DBGPRINT_BUFFER_SIZE"></span>The DbgPrint Buffer Size

The DbgPrint buffer stores messages that the target computer has sent to the kernel debugger.

If Full Kernel Debugging is enabled, these messages will automatically appear in the kernel debugger. But if this option is disabled, these messages will be stored in the buffer. At a later point in time, you can enable kernel debugging, connect to a kernel debugger, and use the [**!dbgprint**](-dbgprint.md) extension to see the contents of this buffer. For more information about this buffer, see The DbgPrint Buffer.

The default size of the DbgPrint buffer is 4 KB on a free build of Windows, and 32 KB on a checked build of Windows. To determine the current buffer size, use **kdbgctrl -cdb**. To change the buffer size, use **kdbgctrl -sdb***Size*, where *Size* specifies the new buffer size. For syntax details, see [**KDbgCtrl Command-Line Options**](kdbgctrl-command-line-options.md).

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

To display all the current settings, use the following command:

```
kdbgctrl -c -ca -cu -cb -cdb 
```

To restore the default settings, use the following command:

```
kdbgctrl -e -da -eu -db -sdb 0x1000 
```

To lock out the host computer so that it only is contacted on exceptions, use the following command:

```
kdbgctrl -d -ea -eu 
```

To disable all kernel debugging, use the following command:

```
kdbgctrl -d -da 
```

If you are disabling all kernel debugging, you may also wish to increase the size of the DbgPrint buffer. This insures that all messages will be saved in case you need to see them later. If you have a megabyte of memory to spare, you might use the following command:

```
kdbgctrl -sdb 0x100000 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20KDbgCtrl%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




