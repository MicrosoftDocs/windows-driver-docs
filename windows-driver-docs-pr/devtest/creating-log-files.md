---
title: Creating Log Files
description: Creating Log Files
ms.assetid: dad0f9fc-1a88-4bee-800a-5a4464fff600
keywords: ["log files WDK Driver Verifier", "Driver Verifier WDK , log files"]
---

# Creating Log Files


## <span id="ddk_creating_log_files_tools"></span><span id="DDK_CREATING_LOG_FILES_TOOLS"></span>


Driver Verifier can create log files. These files will contain periodic updates on a number of statistics related to Driver Verifier's actions and the actions of the drivers being verified.

Log files are created from the Verifier utility by using the **/log** parameter. The frequency of the log record can be specified as well. See [**Verifier Command Line**](verifier-command-line.md) for details.

Each entry will contain both global counters and individual counters, just as with the **verifier /query** command.

For an explanation of these statistics, see [Monitoring Global Counters](monitoring-global-counters.md) and [Monitoring Individual Counters](monitoring-individual-counters.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20Log%20Files%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




