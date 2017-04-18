---
title: How do I generate trace messages from a header file
description: How do I generate trace messages from a header file
ms.assetid: 00b97f26-90e2-4efe-8bba-e3ffe7ba90ea
---

# How do I generate trace messages from a header file?


To generate trace messages from source files with file name extensions other than .c, .c++, .cpp, and .cxx, add the **-ext** parameter to the RUN\_WPP macro that invokes the Windows software trace preprocessor.

For example, to generate traces from .c and .h files, use the following statement:

```
RUN_WPP=$(SOURCES) -km -ext:.c.h
```

The **-ext** parameter specifies the file types that WPP recognizes as source files. WPP ignores files with a different file name extension. By default, WPP recognizes only .c, .c++, .cpp, and .cxx files.

In versions of Windows prior to Windows Vista because the values of this parameter are case-sensitive, you must list all cases. For example:

```
RUN_WPP=$(SOURCES) -km -ext:.c.C.h.H
```

Also, if the header file has the same name as another source file, add the **-preserveext** parameter to the RUN\_WPP macro. For example:

```
RUN_WPP=$(SOURCES) -km -ext:.c.C.h.H  -preserveext:.c.h
```

The **-preserveext** parameter preserves the specified file name extensions when creating the names of [trace message header](trace-message-header-file.md) (.tmh) files. This parameter prevents WPP from creating multiple TMH files with the same name. By default, WPP uses only the .tmh file name extension, such as tracedrv.tmh. With the **-preserveext** parameter, the files are instead named tracedrv.c.tmh and tracedrv.h.tmh.

For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20generate%20trace%20messages%20from%20a%20header%20file?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




