---
title: GPUView Command-Line Options
description: "You can control GPUView from a Command Prompt window."
ms.date: 05/10/2022
---

# GPUView Command-Line Options

You can control GPUView from a Command Prompt window. You can designate switches with either a minus sign (-) or a slash mark (/) followed by either the first character of the option or the full name of the option. The characters are not case sensitive. 

All of the following commands perform the same operation: 

Gpuview /s merged.etl 
Gpuview -s merged.etl 
Gpuview -Stats merged.etl 
Gpuview /staTS merged.etl 
Note that GPUView performs a limited amount of validation on command-line parameters. Therefore, ensure that the syntax of a command is correct to avoid unwanted side effects.

Also, when you issue command-line parameters, the file name, if it is included in the list of parameters, must always be last in the list. There is one exception to this file-name requirement. For more information about this exception, see Option: File. 

The following sections describe the GPUView command-line options:

[Option: Help](option-file.md)

[Option: Stats](option-stats.md)

[Option: Limit](option-limit.md)

[Option: File](option-file.md)
