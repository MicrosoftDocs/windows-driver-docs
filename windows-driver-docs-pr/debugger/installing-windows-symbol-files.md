---
title: Installing Windows Symbol Files
description: Installing Windows Symbol Files
ms.assetid: fbafb14c-9b92-47c5-9954-5c5ba2301c47
keywords: ["symbols, Windows", "symbols, user-mode"]
---

# Installing Windows Symbol Files


## <span id="ddk_installing_windows_symbol_files_dbg"></span><span id="DDK_INSTALLING_WINDOWS_SYMBOL_FILES_DBG"></span>


Before you debug the Windows kernel or a driver or application running on Windows, you need access to the proper symbol files.

If you have access to the internet while your debugger is running, you may wish to use Microsoft's public symbol store. You can connect to this with one simple use of the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command. For full details, see [Microsoft Public Symbols](microsoft-public-symbols.md).

If you plan to install symbols manually, it is crucial that you remember this basic rule: the symbol files on the host computer are required to match the version of Windows installed on the target computer. If you are planning to do a kernel mode debug of a Windows XP target from a Windows 2000 host, you need to install the Windows XP symbol files on the Windows 2000 system. If you plan to perform user-mode debugging on the same computer as the target application, then install the symbol files that match the version of Windows running on that system. If you are analyzing a memory dump file, then the version of symbol files needed on the debug computer are those that match the version of the operating system that produced the dump file, not necessarily those matching the version of the operating system on the machine running the debug session.

**Note**   If you are going to use your host computer to debug several different target computers, you may need symbols for more than one build of Windows. In this case, be sure to install each symbol collection in a distinct directory path.

 

If you are debugging from a Windows computer attached to a network, it may be useful to install symbols for a variety of different builds on a network server. Microsoft debuggers will accept a network path (*\\\\server\\share\\dir*) as a valid symbol directory path. This avoids the need for each debugging computer on the network to install the symbol files separately.

Symbol files stored on a crashed target computer are not usable by the debugger on the host computer.

**To install symbol files for Windows XP or later**

1.  Make sure you have at least 1000 MB of available space on the disk drive of the host computer.

2.  Open the [Windows Symbols](http://go.microsoft.com/fwlink/p/?linkid=17363) Web site in your internet browser.

3.  Follow the links to download the appropriate symbol package.

**To install symbol files for Windows 2000 from the Web**

1.  Make sure you have at least 1000 MB of available space on the disk drive of the host computer.

2.  Open the [Windows Symbols](http://go.microsoft.com/fwlink/p/?linkid=17363) Web site in your internet browser.

3.  Follow the links to download Windows 2000 symbols.

**To install symbol files for Windows 2000 from the Support CD**

1.  Make sure you have at least 500 MB of available space on the disk drive of the host computer.

2.  Insert the Windows 2000 Customer Support Diagnostics CD.

3.  Click **Install Symbols**.

4.  Select either **Install Retail Symbols** (free build) or **Install Debug Symbols** (checked build). The symbols must match the version of the operating system being debugged.

5.  Enter the path where the symbols are to be stored, or accept the default path. The default path is %windir%\\symbols.

### <span id="sequence_of_symbol_file_installation"></span><span id="SEQUENCE_OF_SYMBOL_FILE_INSTALLATION"></span>Sequence of Symbol File Installation

If you intend to keep your symbols in a single directory tree, the installation sequence of symbol files should mirror the installation sequence of operating system files:

**To install the symbol files in correct sequence**

1.  Install the operating system symbol files.

2.  Install the symbol files for the currently installed Service Pack (if any).

3.  Install the symbol files for any Hot Fixes that were installed after the current Service Pack was installed (if any).

However, a superior setup would be to install the symbols from each Service Pack and Hot Fix in a separate directory tree, and put all these directories in your symbol search path. The debugger will then find the proper symbols. (Since the symbol files have date and time stamps, the debugger will be able to tell which are the most recent.) See [Symbol Path](symbol-path.md) for details.

### <span id="installing_user_mode_symbols"></span><span id="INSTALLING_USER_MODE_SYMBOLS"></span>Installing User-Mode Symbols

If you are going to debug a user-mode application, you need to install the symbols for this application as well.

You can debug an application if you have its symbols but not Windows symbols. However, your results will be much more limited. You will still be able to step through the application code, but any debugger activity which requires analysis of the kernel (such as getting a stack trace) is likely to fail.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Installing%20Windows%20Symbol%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




