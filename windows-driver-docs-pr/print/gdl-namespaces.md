---
title: GDL Namespaces
description: GDL Namespaces
ms.assetid: 111bc393-a44a-4c42-98ef-36f6f225b8a0
keywords:
- GDL WDK , namespaces
- namespaces WDK GDL
- namespaces WDK GDL , examples
- unnamed namespaces WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Namespaces


The GDL parser will not allow a template with the same name to be defined more than once. Two independently-written template files can inadvertently use the same name for a template and stop you from including both of these template files in your GDL file.

To avoid name collision problems, GDL supports namespaces. The author of a header file can specify which namespace each template and macro definition should belong to by enclosing the entire definition within a \*DefineInNameSpace construct. The symbol that is supplied as the instance name of this construct will become the namespace that all of the enclosed definitions will belong to. If a definition resides within two or more nested \*DefineInNameSpace constructs, it will belong only to the namespace that is defined by the innermost \*DefineInNameSpace construct. If a definition does not reside within any \*DefineInNameSpace constructs, it will be assigned to the default or "unnamed" namespace.

If entries that comprise the body of a template or macro construct are enclosed within separate \*DefineInNameSpace constructs, the parser will not place those individual entries in the new namespace because the individual entries are not a separate definition, so they cannot live in a different namespace. Block macros permit nested macro definitions, and these nested definitions can be assigned to other namespaces. However, changing the namespace of a nested definition does not extend its lifetime. A nested macro definition can be referenced only within the nesting level that it was defined in.

A template or macro name can be referenced in a qualified or unqualified form in a namespace. To qualify a template or macro name, the namespace name is simply prefixed to the template or macro name with an intervening colon character (for example, *Namespace*:*MacroName*).

**Note**   The symbol name that is supplied as the value of \*Template, \*Macros, or \*BlockMacro definitions cannot be qualified by a namespace. The namespace of a definition can be defined only by using \*DefineInNameSpace.

 

For example, after a template that is named "TEMPNAME" has been defined within a namespace that is named "NSName", that template can be referenced by another template definition by using the namespace qualified form, as the following code example shows.

```cpp
*DefineInNameSpace: NSName
{
    *Template:  TEMPNAME
    {
        *%  member attributes
    }
}
```

This template can now be referenced from another template by using the namespace qualified syntax, as the following code example shows.

```cpp
*Template:  ANOTHER_TEMPLATE
{
    *Inherits: NSName:TEMPNAME
}
```

If the majority of template references will reference the same namespace or if there is no name collision between template names that are referenced within two or more namespaces, you can omit the namespace qualifier and supply only the template name and rely on the parser to search a list of namespaces until a matching template is found.

The list of namespaces is specified by enclosing one or more GDL entries within \*UsingNameSpace constructs. If any of these entries contain unqualified references to a template or macro, the resolution of those references will be affected by the \*UsingNameSpace constructs. The symbol that is supplied as the instance name of this construct identifies the namespace to be searched.

You can specify multiple namespaces by nesting several constructs. The search order starts with the innermost \*UsingNameSpace construct and proceeds outward. If a template definition is found in a specified namespace, the search stops and that template is used. If no match has been found after all of the explicitly specified namespaces have been searched, the parser will search the namespace that is named in each enclosing \*DefineInNameSpace construct from innermost construct outwards. And if that search fails to resolve the reference, it will attempt to search the "unnamed" namespace.

**Note**   If you need to insulate the namespace search order from outside influences, all of the namespaces that are needed to resolve references should be specified by using \*UsingNameSpace constructs.

 

You should not rely on the \*DefineInNameSpace construct to establish the search order because the host might surround the included file with additional \*UsingNameSpace constructs and the host-specified namespaces will be searched before the namespaces that are named by the \*DefineInNameSpace constructs.

For example, the template that was defined earlier showed two namespaces that have been explicitly specified to be used for template name resolution. Any namespace that is named by \*UsingNameSpace must have been previously defined by \*DefineInNameSpace. The exception is the "unnamed" namespace, which always exists and is named by the NULL symbol.

The following code example shows how to specify the "unnamed" namespace to define the search order.

```cpp
*UsingNameSpace: NSName2
{
    *UsingNameSpace:  *%%%%%  omitting symbol specifies the  Unnamed 
*%  Namespace.
    {
        *UsingNameSpace: NSName
        {
            *Template:  ANOTHER_TEMPLATE
            {
                *Inherits: TEMPNAME
            }
        }
    }
}
```

In the preceding example, the "unnamed" namespace will be searched after all searches in the explicitly specified namespace have failed, but the example explicitly specifies that the "unnamed" namespace be searched before the NSName2 namespace.

Because GDL data entries never explicitly reference template names, the use of \*UsingNameSpace will not affect which template is assigned to each data entry. However, the namespace search order that \*UsingNameSpace specifies (which is in effect at the time the first GDL data entry is parsed) is used in search for the ROOT template. If you are including one or more GDL header files, you should ensure that they do not inadvertently become the first to define a data entry and hence determine which namespace is used to find the ROOT template.

**Note**   Macro definitions are scope-limited by the enclosing nesting level. However, namespace nesting levels do not limit the scope of macro definitions because you do not need to define a macro to belong to a particular namespace if the scope of the macro is not large enough to be visible outside of that namespace.

 

Namespace constructs can be interleaved between other types of constructs. There is almost no restriction on where a namespace construct can appear. The non-namespace constructs do not affect namespace resolution.

 

 




