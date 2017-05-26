---
title: .dml\_start (Display DML Starting Point)
description: The .dml\_start command displays output that serves as a starting point for exploration using commands that support Debugger Markup Language (DML).
ms.assetid: 1CFCACDC-B253-4E9B-9877-EE9F1E91395F
keywords: [".dml_start (Display DML Starting Point) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .dml_start (Display DML Starting Point)
api_type:
- NA
---

# .dml\_start (Display DML Starting Point)


The **.dml\_start** command displays output that serves as a starting point for exploration using commands that support [Debugger Markup Language](debugger-markup-language-commands.md) (DML).

```
.dml_start
.dml_start filename
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="filename"></span><span id="FILENAME"></span>*filename*  
The name of a DML file to be displayed as the starting output.

## <span id="Using_the_Default_Starting_Output"></span><span id="using_the_default_starting_output"></span><span id="USING_THE_DEFAULT_STARTING_OUTPUT"></span>Using the Default Starting Output


If *filename* is omitted, the debugger displays a default DML starting output as illustrated in the following image.

![screen shot of .dml\-start output](images/dmlstart01.png)

Each line of output in the preceding example is a link that you can click to invoke other commands.

## <span id="Providing_a_DML_File"></span><span id="providing_a_dml_file"></span><span id="PROVIDING_A_DML_FILE"></span>Providing a DML File


If you supply a path to a DML file, the file is used as the starting output. For example, suppose the file c:\\MyFavoriteCommands.txt contains the following text and DML tags.

```
Display all device nodes.
   <link cmd="!devnode 0 1">!devnode 0 1</link>

Display all device nodes that are driven by a specified service.
Include child nodes in the display.
   <b>!devnode 0 1</b> <i>ServiceName</i>  
   Example: <link cmd="!devnode 0 1 usbehci">!devnode 0 1 usbehci</link>

Explore device stacks, device objects, and driver objects.
   <b>!devstack</b>  List the device objects in a device stack.
   <b>!devobj</b>    Display information about a device object.
   <b>!drvobj</b>    Display information about a driver object.
```

The command **.dml\_start c:\\MyFavoriteCommands.txt** will display the file as shown in the following image.

![screen shot of dml file output](images/dmlstart02.png)

Remarks
-------

For information about DML tags that can be used in DML files, see dml.doc in the installation folder for Debugging Tools for Windows.

DML output often works well in the [Command Browser window](command-browser-window.md). To display a DML file in the Command Browser window, use **.browse .dml\_start** *filename*.

## <span id="see_also"></span>See also


[Debugger Markup Language Commands](debugger-markup-language-commands.md)

[**.browse**](-browse--display-command-in-browser-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.dml_start%20%28Display%20DML%20Starting%20Point%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





