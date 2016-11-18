---
title: BinPlace Macros and Environment Variables
description: BinPlace Macros and Environment Variables
ms.assetid: f990e132-f6d7-46e1-8c86-6ae3f0483bd5
keywords: ["BinPlace WDK , environment variables", "environment variables WDK BinPlace"]
---

# BinPlace Macros and Environment Variables


## <span id="ddk_binplace_environment_variables_tools"></span><span id="DDK_BINPLACE_ENVIRONMENT_VARIABLES_TOOLS"></span>


BinPlace reads the values of the following macros and environment variables:

<span id="BINPLACE_OVERRIDE_FLAGS"></span><span id="binplace_override_flags"></span>BINPLACE\_OVERRIDE\_FLAGS  
Specifies a file that contains additional command-line parameters. BinPlace will use these switches as well as those on the actual command line. The switches in this override file will be parsed before the actual command-line switches.

<span id="________BINPLACE_LOG_______"></span><span id="________binplace_log_______"></span> BINPLACE\_LOG   
Specifies the path and file name of the log file. All BinPlace actions will be recorded in this log file.

<span id="BINPLACE_MESSAGE_LOG"></span><span id="binplace_message_log"></span>BINPLACE\_MESSAGE\_LOG  
Specifies the path and file name of the message log file. Each time BinPlace is executed, its command line will be recorded in the message log file. If the command line is expanded using files prefixed with an at sign ( **@** ), the expanded command-line text will be stored in the message log. However, parameters originating in the BINPLACE\_OVERRIDE\_FLAGS file will not be recorded in the message log file.

<span id="BINPLACE_EXCLUDE_FILE"></span><span id="binplace_exclude_file"></span>BINPLACE\_EXCLUDE\_FILE  
Specifies the path and file name of the exclude file. If this is not present, the default is \\tools\\symbad.txt. This file will be used by SymChk as if it were the argument of SymChk's **/ea** switch. (SymChk is part of the Debugging Tools for Windows package. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for details.)

<span id="TRACE_FORMAT_PATH"></span><span id="trace_format_path"></span>TRACE\_FORMAT\_PATH  
Specifies the path to be used for trace format files when the **-:TMF** switch is used.

<span id="_________NTTREE_______"></span><span id="_________nttree_______"></span> \_NTTREE   
Specifies the root destination directory in which all files will be placed if the **-r** switch is not used. For more information, see [BinPlace Destination Directories](binplace-destination-directories.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20BinPlace%20Macros%20and%20Environment%20Variables%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




