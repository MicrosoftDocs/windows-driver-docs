---
title: .dml_start (Display DML Starting Point)
description: The .dml_start command displays output that serves as a starting point for exploration using commands that support Debugger Markup Language (DML).
keywords: [".dml_start (Display DML Starting Point) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .dml_start (Display DML Starting Point)
api_type:
- NA
---

# .dml\_start (Display DML Starting Point)

The **.dml\_start** command displays output that serves as a starting point for exploration using commands that support [Debugger Markup Language](../debugger/debugger-markup-language-commands.md) (DML).

```dbgcmd
.dml_start
.dml_start filename
```

## Parameters

<span id="filename"></span><span id="FILENAME"></span>*filename*  
The name of a DML file to be displayed as the starting output.

## Using the Default Starting Output

If *filename* is omitted, the debugger displays a default DML starting output as illustrated in the following image.

:::image type="content" source="images/dmlstart01.png" alt-text="Screenshot of the default .dml-start output.":::

Each line of output in the preceding example is a link that you can click to invoke other commands.

## Providing a DML File

If you supply a path to a DML file, the file is used as the starting output. For example, suppose the file c:\\MyFavoriteCommands.txt contains the following text and DML tags.

```dbgcmd
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

:::image type="content" source="images/dmlstart02.png" alt-text="Screenshot of the output from a custom DML file.":::

## Remarks

For information about DML tags that can be used in DML files, see dml.doc in the installation folder for Debugging Tools for Windows.

DML output often works well in the [Command Browser window](../debugger/command-browser-window.md). To display a DML file in the Command Browser window, use **.browse .dml\_start** *filename*.

## See also

[Debugger Markup Language Commands](../debugger/debugger-markup-language-commands.md)

[**.browse**](-browse--display-command-in-browser-.md)
