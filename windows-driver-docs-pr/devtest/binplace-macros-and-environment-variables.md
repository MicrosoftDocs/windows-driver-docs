---
title: BinPlace Macros and Environment Variables
description: BinPlace Macros and Environment Variables
ms.assetid: f990e132-f6d7-46e1-8c86-6ae3f0483bd5
keywords:
- BinPlace WDK , environment variables
- environment variables WDK BinPlace
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





