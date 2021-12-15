---
title: Native Debugger Objects in JavaScript Extensions - Type Objects
description: Native debugger objects represent various constructs of the debugger environment. JavaScript extensions have direct access to the type system of the underlying language. This access is expressed through the notion of type objects.
ms.date: 02/04/2021
---

# Native Debugger Objects in JavaScript Extensions - Type Objects

 Native debugger objects represent various constructs of the debugger environment. JavaScript extensions have direct access to the type system of the underlying language. This access is expressed through the notion of *type objects*. This topic describes the properties associated with type objects.

Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions to manipulate the state of the debugger.

For information about Debugger object JavaScript extensions, see [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

For general information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md).

## Type Objects

A type object can be acquired in a number of ways:

- From an Object: If a script has a native object within JavaScript, the *targetType* property can be accessed on that object in order to get a *type object* representing the static type of the native object.
- From the Host: The *host.getModuleType* API can be called in order to return the *type object* for any type defined in a particular module.

Once the type object is acquired, it has the following properties:

<table>
<tr><td><b>Name</b></td><td><b>Signature</b></td><td><b>Description</b></td></tr>

<tr><td>name</td><td>Property</td><td>Returns the name of the type.</td></tr>

<tr><td>size</td><td>Property</td><td>Returns the size of the type as a 64-bit value.</td></tr>

<tr><td>typeKind</td><td>Property</td><td>Returns the kind of the type as a string.  This can be one of the following values: "udt", "pointer", "memberPointer", "array", "function", "typedef", "enum", or "intrinsic".</td></tr>

<tr><td>baseType</td><td>Property</td><td>Returns a type object for the type on which this type is based.  This does not represent C++ inheritance.  For a pointer type, this is the type of the thing pointed to.  For an array type, this is the type contained in the array.</td></tr>

<tr><td>fields</td><td>Property</td><td>Returns an object which has all the named fields of the type accessible as named properties.  The value of each property is a <i>field object</i> as described below.</td></tr>

<tr><td>baseClasses</td><td>Property</td><td>Returns an array of all the immediate base classes of the type.  Each object in the array is a <i>base class object</i> as described below.</td></tr>

<tr><td>functionReturnType</td><td>Property</td><td>For function types, this returns a type object representing the return type of the function.</td></tr>

<tr><td>functionParameterTypes</td><td>Property</td><td>For function types, this returns an array of type objects representing the parameter types of the function.</td></tr>

<tr><td>functionCallingConvention</td><td>Property</td><td>For function types, this returns the calling convention of the function as a string.  This can be one of the following values: "unknown", "__cdecl", "fastcall", "stdcall", or "thiscall".</td></tr>

<tr><td>pointerKind</td><td>Property</td><td>For pointer types, this returns the kind of pointer as a string.  This can be one of the following values: "standard", "reference", "rValueReference", or "cxHat".</td></tr>

<tr><td>memberType</td><td>Property</td><td>For pointer types which are member pointers, this returns a type object representing the member class.</td></tr>

<tr><td>isGeneric</td><td>Property</td><td>Returns whether the type is generic or not.  This will return true for template types.</td></tr>

<tr><td>genericArguments</td><td>Property</td><td>For types which are generic, this will return an array of generic arguments.  Such arguments may be type arguments or may be constant values.</td></tr>

<tr><td>isBitField</td><td>Property</td><td>Returns whether the storage for the type is a bitfield or not.</td></tr>

<tr><td>bitFieldPositions</td><td>Property</td><td>For types which represent bitfield storage, this will return a bit field description type indicating the positions of the bitfield.</td></tr>

</table>

All of these entries are present during phase 2 initialization.

## Field Objects

Each field within a type is described by a field object having properties as follows:

<table>

<tr><td><b>Name</b></td><td><b>Signature</b></td><td><b>Description</b></td></tr>

<tr><td>name</td><td>Property</td><td>Returns the name of the field.</td></tr>

<tr><td>type</td><td>Property</td><td>Returns a type object representing the static type of the field.</td></tr>

<tr><td>locationKind</td><td>Property</td><td>Returns the location kind (storage) for the field as a string.  This can be one of the following values: "member", "static", "constant", or "none".</td></tr>

<tr><td>offset</td><td>Property</td><td>For fields which have a location kind that indicates an offset (e.g.: "member"), this returns the offset of the field within its containing type as a 64-bit value.</td></tr>

<tr><td>location</td><td>Property</td><td>For fields which have a location kind that indicates a location (e.g.: "static"), this returns the location of the field as a <i>location object.</i></td></tr>

<tr><td>value</td><td>Property</td><td>For fields which have a location kind that indicates a value (e.g.: "constant"), this returns the value of the field.</td></tr>

</table>

All of these entries are present during phase 2 initialization.

## Base Class Objects

Each base class within a type is described by a base class object having properties as follows:

<table>

<tr><td><b>Name</b></td><td><b>Signature</b></td><td><b>Description</b></td></tr>

<tr><td>name</td><td>Property</td><td>Returns the name of the base class.</td></tr>

<tr><td>offset</td><td>Property</td><td>Returns the offset of this base class within its containing type.</td></tr>

<tr><td>type</td><td>Property</td><td>Returns a type object representing the static type of the base class.</td></tr>

</table>

All of these entries are present during phase 2 initialization.

## Code Example

For a code example, see the ImageInfo.js script. For more information on code samples, see [JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md).

```javascript
// fieldType references basic types that should be present in **ANY** symbolic information.
// Just grab the first module as the "reference module" for this purpose.  We cannot grab
// "ntdll" generically as we want to avoid a situation in which the debugger opens a module (-z ...)
// from failing.
//
var moduleName = contextInheritorModule.__ComparisonName;
var typeObject = host.getModuleType(moduleName, field.fieldType, contextInheritorModule);
var result = host.createTypedObject(addr, typeObject);

```

## <span id="related_topics"></span>Related topics

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

[Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations](native-objects-in-javascript-extensions-design-considerations.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)
