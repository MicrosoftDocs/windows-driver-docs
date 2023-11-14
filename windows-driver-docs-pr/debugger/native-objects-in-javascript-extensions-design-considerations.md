---
title: Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations
description: Native debugger objects represent various constructs of the debugger environment. This topic describes design and testing considerations for native debugger objects in JavaScript extensions.
ms.date: 09/07/2019
---

# Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations

This topic describes design and testing considerations for using the native debugger objects in JavaScript extensions.

Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions to manipulate the state of the debugger.

For information about Debugger object JavaScript extensions, see [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

For general information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md).

## Debugger Data Model Design Considerations

**Design Principles**

Consider the following principles to make your debugger extensions present information that is discoverable, queryable, and scriptable.

- Information is close to where it is needed. For example, information on a registry key should be displayed as part of a local variable that contains a registry key handle.
- Information is structured. For example, information about a registry key is presented in separate fields such as key type, key ACL, key name, and value. This means that the individual fields can be accessed without parsing text.
- Information is consistent. Information about registry key handles is presented in as similar a way as possible to information about file handles.

Avoid these approaches that do not support these principles.

- Do not structure your items into a single flat "Kitchen sink". An organized hierarchy allows users to browse for the information they are looking for without prior knowledge of what they are looking for and supports discoverability.
- Do not convert a classic dbgeng extension by simply moving it to the model while still outputting screens of raw text. This is not composable with other extensions and cannot be queried with LINQ expressions. Instead break the data into separate, queryable fields.

**Naming Guidelines**

- Capitalization of fields should be PascalCase. An exception could be considered for names that are widely known in another casing, such as jQuery.
- Avoid using special characters that would not normally be used in a C++ identifier. For example, avoid using names such as "Total Length" (that contains a space), or "\[size\]" (that contains square brackets). This convention allows for easier consumption from scripting languages where these characters are not allowed as part of identifiers, and also allows easier consumption from the command window.

**Organization and Hierarchy Guidelines**

- Do not extend the top level of the debugger namespace. Instead, you should extend an existing node in the debugger so that the information is displayed where it is most relevant.
- Do not duplicate concepts. If you are creating a data model extension that lists additional information about a concept that already exists in the debugger, extend the existing information rather than trying to replace it with new information. In other words, an extension that displays details about a module should extend the existing *Module* object rather than creating a new list of modules.
- Free floating utility commands must be part of the *Debugger.Utility* namespace. They should also be sub-namespaced appropriately (e.g. *Debugger.Utility.Collections.FromListEntry*)

**Backwards Compatibility and Breaking Changes**

A script that is published should not break compatibility with other scripts that depend on it. For example, if a function is published to the model, it should remain in the same location and with the same parameters, whenever possible.

**No Use of Outside Resources**

- Extensions must not spawn external processes. External processes can interfere with the behavior of the debugger, and will misbehave in various remote debugger scenarios (e.g. dbgsrv remotes, ntsd remotes, and "ntsd -d remotes")
- Extensions must not display any user interface. Displaying user interface elements will behave incorrectly on remote debugging scenarios, and can break console debugging scenarios.
- Extensions must not manipulate the debugger engine or debugger UI through undocumented methods. This causes compatibility problems and will behave incorrectly on debugger clients with different UI.
- Extensions must access target information only through the documented debugger APIs. Trying to access information about a target through win32 APIs will fail for many remote scenarios, and even some local debugging scenarios across security boundaries.

**No Use of Dbgeng Specific Features**

Scripts that are intended to be used as extensions must not rely on dbgeng-specific features whenever possible (such as executing "classic" debugger extensions). Scripts should be usable on top of any debugger that hosts the data model.

## Testing Debugger Extensions

Extensions are expected to work in a wide range of scenarios. While some extensions may be specific to a scenario (such as a kernel debugging scenario), most extensions should be expected to work in all scenarios, or have metadata indicating the supported scenarios.

Kernel Mode

- Live kernel debugging
- Kernel dump debugging

User Mode

- Live user mode debugging
- User mode dump debugging

In addition, consider these debugger usage scenarios

- Multi-process debugging
- Multi-session debugging (e.g. dump + live user within a single session)

**Remote Debugger Usage**

Test for proper operation with the remote debugger usage scenarios.

- dbgsrv remotes
- ntsd remotes
- ntsd -d remotes

For more information, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md) and [**Activating a Process Server**](activating-a-process-server.md).

**Regression testing**

Investigate the use of test automation that can verify the functionality of your extensions, as new versions of the debugger are released.

## See also

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

[Native Debugger Objects in JavaScript Extensions - Debugger Object Details](native-objects-in-javascript-extensions-debugger-objects.md).

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)
