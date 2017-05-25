---
title: dml\_proc
description: The dml\_proc extension displays a list of processes and provides links for obtaining more detailed information about processes.
ms.assetid: 35B5B2E7-07CE-4F44-819D-9B7C76273F9A
keywords: ["dml_proc Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- dml_proc
api_type:
- NA
---

# !dml\_proc


The **!dml\_proc** extension displays a list of processes and provides links for obtaining more detailed information about processes.

``` syntax
!dml_proc
```

Remarks
-------

The following image shows a portion of the output displayed by **!dml\_proc**.

![screen shot of !dml\-proc output](images/dmlproc01.png)

In the preceding output, the process addresses are links that you can click to see more detailed information. For example, if you click **fffffa80\`04e2b700** (the address for mobsync.exe), you will see detailed information about the mobsync.exe process as shown in the following image.

![screen shot of process details](images/dmlproc02.png)

The preceding output, which describes an individual process, contains links that you can click to explore the process and its threads in more detail.

## <span id="see_also"></span>See also


[Debugger Markup Language Commands](debugger-markup-language-commands.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dml_proc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





