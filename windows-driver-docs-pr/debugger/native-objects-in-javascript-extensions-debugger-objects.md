---
title: Native Debugger Objects in JavaScript Extensions - Debugger Object Details
description: Native debugger objects represent various constructs of the debugger environment. This topic describes additional details about the native debugger objects in JavaScript extensions.
ms.date: 02/02/2021
ms.localizationpriority: medium
---

# Native Debugger Objects in JavaScript Extensions - Debugger Object Details

This topic describes additional details about using the native debugger objects in JavaScript extensions.

Native debugger objects represent various constructs and behaviors of the debugger environment. The objects can be passed into (or acquired in) JavaScript extensions to manipulate the state of the debugger.

For information about Debugger object JavaScript extensions, see [Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

For general information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md).

For example JavaScript scripts and extensions, the debugger team hosts a GitHub repo at https://github.com/Microsoft/WinDbg-Samples.

## <span id="Debugger-Objects"></span><span id="debugger-objects"></span><span id="DEBUGGER-OBJECTS"></span>Debugger Objects in JavaScript Extensions

**Passing Native Objects**

Debugger objects can be passed into or acquired in JavaScript extensions in a variety of ways.

-   They can be passed to JavaScript functions or methods
-   They can be the instance object for a JavaScript prototype (as a visualizer, for instance)
-   They can be returned from host methods designed to create native debugger objects
-   They can be returned from host methods designed to create debugger native objects

Debugger objects that are passed to a JavaScript extension have a set of functionality that is described in this section.

-   Property Access
-   Projected Names
-   Special Types Pertaining to Native Debugger Objects
-   Additional Attributes

**Property Access**

While there are some properties on objects which are placed there by the JavaScript provider itself, the majority of properties on a native object which enters JavaScript are provided by the data model. This means that for a property access --- object.propertyName or object\[propertyName\], the following will occur.

-   If *propertyName* is the name of a property projected onto the object by the JavaScript provider itself, it will resolve to this first; otherwise
-   If *propertyName* is the name of a key projected onto the object by the data model (another Visualizer), it will resolve to this name second; otherwise
-   If *propertyName* is the name of a field of the native object, it will resolve to this name third; otherwise
-   If object is a pointer, the pointer will be dereferenced, and the cycle above will continue (a projected property of the dereferenced object followed by a key followed by a native field)

The normal means of property access in JavaScript -- object.propertyName and object\[propertyName\] -- will access the underlying native fields of an object, much as the 'dx' command would within the debugger.

**Projected Names**

The following properties (and methods) are projected onto native objects which enter JavaScript.

| Method             | Signature                  | Description                                                                                                                                |
|--------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| hostContext        | Property                   | Returns an object which represents the context the object is within (the address space, debug target, etc...)                              |
| targetLocation     | Property                   | Returns an object which is an abstraction of where the object is within an address space (virtual address, register, sub-register, etc...) |
| targetSize         | Property                   | Returns the size of the object (effectively: sizeof(&lt;TYPE OF OBJECT&gt;)                                                                |
| addParentModel     | .addParentModel(object)    | Adds a new parent model (akin to a JavaScript prototype but on the data model side) to the object                                          |
| removeParentModel  | .removeParentModel(object) | Removes a given parent model from the object                                                                                               |
| runtimeTypedObject | Property                   | Performs analysis on the object and tries to convert it to the runtime (most derived) type                                                 |
| targetType         | Property                   | JavaScript extensions have direct access to the type system of the underlying language. This access is expressed through the notion of type objects. For more information, see [Native Debugger Objects in JavaScript Extensions - Type Objects](native-objects-in-javascript-extensions-type-objects.md)  |

If the object is a pointer, the following properties (and methods) are projected onto the pointer which enters JavaScript:

| Property Name | Signature      | Description                                                                    |
|---------------|----------------|--------------------------------------------------------------------------------|
| add           | .add(value)    | Performs pointer math addition between the pointer and the specified value     |
| address       | Property       | Returns the address of the pointer as a 64-bit ordinal object (a library type) |
| dereference   | .dereference() | Dereferences the pointer and returns the underlying object                     |
| isNull        | Property       | Returns whether or not the pointer value is nullptr (0)                        |

**Special Types Pertaining to Native Debugger Objects**

**Location Objects**

The location object which is returned from the targetLocation property of a native object contains the following properties (and methods).

| Property Name | Signature        | Description                                          |
|---------------|------------------|------------------------------------------------------|
| add           | .add(value)      | Adds an absolute byte offset to the location.        |
| subtract      | .subtract(value) | Subtracts an absolute byte offset from the location. |

**Additional Attributes**

**Iterability**

Any object which is understood as iterable by the data model (it is a native array or it has a visualizer (NatVis or otherwise) which makes it iterable) will have an iterator function (indexed via the ES6 standard Symbol.iterator) placed upon it. This means that you can iterate a native object in JavaScript as follows.

```javascript
function iterateNative(nativeObject)
{
    for (var val of nativeObject)
    {
        // 
        // val will contain each element iterated from the native object.  This would be each element of an array,
        // each element of an STL structure which is made iterable through NatVis, each element of a data structure
        // which has a JavaScript iterator accessible via [Symbol.iterator], or each element of something
        // which is made iterable via support of IIterableConcept in C/C++.
        //
    }
}
```

**Indexability**

Objects which are understood as indexable in one dimension via ordinals (e.g.: native arrays) will be indexable in JavaScript via the standard property access operator -- object\[index\]. If an object is indexable by name or is indexable in more than one dimension, the getValueAt and setValueAt methods will be projected onto the object so that JavaScript code can utilize the indexer.

```javascript
function indexNative(nativeArray)
{
    var first = nativeArray[0];
}
```

**String Conversion**

Any native object which has a display string conversion via support of IStringDisplayableConcept or a NatVis DisplayString element will have that string conversion accessible via the standard JavaScript toString method.

```javascript
function stringifyNative(nativeObject)
{
    var myString = nativeObject.toString();
}
```

## <span id="Creating_Native_Debugger_Objects"></span><span id="creating_native_debugger_objects"></span><span id="CREATING_NATIVE_DEBUGGER_OBJECTS"></span>Creating Native Debugger Objects

As mentioned, a JavaScript script can get access to native objects by having them passed into JavaScript in one of several ways or it can create them through calls to the host library. Use the following functions to create native debugger objects.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Signature</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>host.getModuleSymbol</p></td>
<td align="left"><p>getModuleSymbol(moduleName, symbolName, [contextInheritor])</p>
<p>getModuleSymbol(moduleName, symbolName, [typeName], [contextInheritor])</p></td>
<td align="left"><p>Returns an object for a global symbol within a particular module. The module name and symbol name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger's current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p>
<p>If the optional <em>typeName</em> argument is supplied, the symbol will be assumed to be of the passed type and the type indicated in symbol(s) will be ignored. Note that any caller which expects to operate on public symbols for a module should always supply an explicit type name.</p></td>
</tr>
<tr>
<td align="left"><p>host.getModuleContainingSymbol</p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>host.createPointerObject</p></td>
<td align="left"><p>createPointerObject(address, moduleName, typeName, [contextInheritor])</p></td>
<td align="left"><p>Creates a pointer object at the specified address or location. The module name and type name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger's current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>host.createTypedObject</p></td>
<td align="left"><p>createTypedObject(location, moduleName, typeName, [contextInheritor])</p></td>
<td align="left"><p>Creates a object which represents a native typed object within the address space of a debug target at the specified location. The module name and type name are strings.</p>
<p>If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger's current context. A JavaScript extension which is not a one-off test script should always supply an explicit context.</p></td>
</tr>
</tbody>
</table>

## <span id="Host-APIs"></span><span id="host-apis"></span><span id="HOST-APIS"></span>Host APIs for JavaScript Extensions

The JavaScript provider inserts an object called host into the global namespace of every script which it loads. This object provides access to critical functionality for the script as well as access to the namespace of the debugger. It is set up in two phases.

-   **Phase 1**: Before any script executes, the host object only contains the minimal set of functionality necessary for a script to initialize itself and register its extensibility points (both as producer and consumer). The root and initialization code is not intended to manipulate the state of a debug target or perform complex operations and, as such, the host is not fully populated until after the initializeScript method returns.

-   **Phase 2**: After initializeScript returns, the host object is populated with everything necessary to manipulate the state of debug targets.

**Host Object Level**

A few key pieces of functionality are directly under the host object. The remainder are sub-namespaced. Namespaces include the following.

| Namespace   | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| diagnostics | Functionality to assist in the diagnosis and debugging of script code    |
| memory      | Functionality to enable memory reading and writing within a debug target |

**Root Level**

Directly within the host object, the following properties, methods, and constructors can be found.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="30%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Signature</th>
<th align="left">Phase Present</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">createPointerObject</td>
<td align="left"><p>createPointerObject(address, moduleName, typeName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Creates a pointer object at the specified address or location. The module name and type name are strings. The optional <strong>contextInheritor</strong> argument works as with getModuleSymbol.</td>
</tr>
<tr class="even">
<td align="left">createTypedObject</td>
<td align="left"><p>createTypedObject(location, moduleName, typeName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Creates a object which represents a native typed object within the address space of a debug target at the specified location. The module name and type name are strings. The optional contextInheritor argument works as with getModuleSymbol.</td>
</tr>
<tr class="odd">
<td align="left">currentProcess</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current process of the debugger</td>
</tr>
<tr class="even">
<td align="left">currentSession</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current session of the debugger (which target, dump, etc...) is being debugged</td>
</tr>
<tr class="odd">
<td align="left">currentThread</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Returns the object representing the current thread of the debugger</td>
</tr>
<tr class="even">
<td align="left">evaluateExpression</td>
<td align="left"><p>evaluateExpression(expression, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This calls into the debug host to evaluate an expression using the language of the debug target only. If the optional <em>contextInheritor</em> argument is supplied, the expression will be evaluated in the context (e.g.: address space and debug target) of the argument; otherwise, it will be evaluated in the current context of the debugger</td>
</tr>
<tr class="odd">
<td align="left">evaluateExpressionInContext</td>
<td align="left"><p>evaluateExpressionInContext(context, expression)</p></td>
<td align="left">2</td>
<td align="left">This calls into the debug host to evaluate an expression using the language of the debug target only. The context argument indicates the implicit this pointer to utilize for the evaluation. The expression will be evaluated in the context (e.g.: address space and debug target) indicated by the <em>context</em> argument.</td>
</tr>
<tr class="even">
<td align="left">getModuleSymbol</td>
<td align="left"><p>getModuleSymbol(moduleName, symbolName, [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">Returns an object for a global symbol within a particular module. The module name and symbol name are strings. If the optional <em>contextInheritor</em> argument is supplied, the module and symbol will be looked up within the same context (address space, debug target) as the passed object. If the argument is not supplied, the module and symbol will be looked up in the debugger's current context. A JavaScript extension which is not a one-off script should always supply an explicit context</td>
</tr>
<tr class="odd">
<td align="left">getNamedModel</td>
<td align="left"><p>getNamedModel(modelName)</p></td>
<td align="left">2</td>
<td align="left">Returns the data model which was registered against a given name. Note that it is perfectly legal to call this against a name which is not yet registered. Doing so will create a stub for that name and manipulations of the stub will be made to the actual object upon registration</td>
</tr>
<tr class="even">
<td align="left">indexedValue</td>
<td align="left"><p>new indexedValue(value, indicies)</p></td>
<td align="left">2</td>
<td align="left">A constructor for an object which can be returned from a JavaScript iterator in order to assign a default set of indicies to the iterated value. The set of indicies must be expressed as a JavaScript array.</td>
</tr>
<tr class="odd">
<td align="left">Int64</td>
<td align="left"><p>new Int64(value, [highValue])</p></td>
<td align="left">1</td>
<td align="left">This constructs a library Int64 type. The single argument version will take any value which can pack into an Int64 (without conversion) and place it into such. If an optional second argument is supplied, a conversion of the first argument is packed into the lower 32-bits and a conversion of the second argument is packed into the upper 32 bits.</td>
</tr>
<tr class="even">
<td align="left">namedModelParent</td>
<td align="left"><p>new namedModelParent(object, name)</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents using a JavaScript prototype or ES6 class as a data model parent extension of a data model with the given name</td>
</tr>
<tr class="odd">
<td align="left">namedModelRegistration</td>
<td align="left"><p>new namedModelRegistration(object, name)</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents the registration of a JavaScript prototype or ES6 class as a data model via a known name so that other extensions can find and extend</td>
</tr>
<tr class="even">
<td align="left">namespace</td>
<td align="left"><p>Property</p></td>
<td align="left">2</td>
<td align="left">Gives direct access to the root namespace of the debugger. One could, for example, access the process list of the first debug target via host.namespace.Debugger.Sessions.First().Processes using this property</td>
</tr>
<tr class="odd">
<td align="left">registerNamedModel</td>
<td align="left"><p>registerNamedModel(object, modelName)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as a data model under the given name. Such a registration allows the prototype or class to be located and extended by other scripts or other debugger extensions. Note that a script should prefer to return a <strong>namedModelRegistration</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up.</td>
</tr>
<tr class="even">
<td align="left">registerExtensionForTypeSignature</td>
<td align="left"><p>registerExtensionForTypeSignature(object, typeSignature)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as an extension data model for a native type as given by the supplied type signature. Note that a script should prefer to return a <strong>typeSignatureExtension</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up.</td>
</tr>
<tr class="odd">
<td align="left">registerPrototypeForTypeSignature</td>
<td align="left"><p>registerPrototypeForTypeSignature(object, typeSignature)</p></td>
<td align="left">2</td>
<td align="left">This registers a JavaScript prototype or ES6 class as the canonical data model (e.g.: visualizer) for a native type as given by the supplied type signature. Note that a script should prefer to return a <strong>typeSignatureRegistration</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>uninitializeScript</strong>method in order to clean up.</td>
</tr>
<tr class="even">
<td align="left">parseInt64</td>
<td align="left"><p>parseInt64(string, [radix])</p></td>
<td align="left">1</td>
<td align="left">This method acts similarly to the standard JavaScript parseInt method except that it returns a library Int64 type instead. If a radix is supplied, the parse will occur in either base 2, 8, 10, or 16 as indicated.</td>
</tr>
<tr class="odd">
<td align="left">typeSignatureExtension</td>
<td align="left"><p>new typeSignatureExtension(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents an extension of a native type described via a type signature by a JavaScript prototype or ES6 class. Such a registration "adds fields" to the debugger's visualization of any type which matches the signature rather than taking it over entirely. An optional module name and version can restrict the registration. Versions are specified as "1.2.3.4" style strings.</td>
</tr>
<tr class="even">
<td align="left">typeSignatureRegistration</td>
<td align="left"><p>new typeSignatureRegistration(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">1</td>
<td align="left">A constructor for an object intended to be placed in the array returned from <strong>initializeScript</strong>, this represents a canonical registration of a JavaScript prototype or ES6 class against a native type signature. Such a registration "takes over" the debugger's visualization of any type which matches the signature rather than merely than extending it. An optional module name and version can restrict the registration. Versions are specified as "1.2.3.4" style strings.</td>
</tr>
<tr class="odd">
<td align="left">unregisterNamedModel</td>
<td align="left"><p>unregisterNamedModel(modelName)</p></td>
<td align="left">2</td>
<td align="left">This unregisters a data model from lookup by the given name undoing any operation performed by <strong>registerNamedModel</strong></td>
</tr>
<tr class="even">
<td align="left">unregisterExtensionForTypeSignature</td>
<td align="left"><p>unregisterExtensionForTypeSignature(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">2</td>
<td align="left">This unregisters a JavaScript prototype or ES6 class from being an extension data model for a native type as given by the supplied type signature. It is the logical undo of registerExtensionForTypeSignature. Note that a script should prefer to return a <strong>typeSignatureExtension</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>initializeScript</strong> method in order to clean up. An optional module name and version can restrict the registration. Versions are specified as "1.2.3.4" style strings.</td>
</tr>
<tr class="odd">
<td align="left">unregisterPrototypeForTypeSignature</td>
<td align="left"><p>unregisterPrototypeForTypeSignature(object, typeSignature, [moduleName], [minVersion], [maxVersion])</p></td>
<td align="left">2</td>
<td align="left">This unregisters a JavaScript prototype or ES6 class from being the canonical data model (e.g.: visualizer) for a native type as given by the supplied type signature. It is the logical undo of registerPrototypeForTypeSignature. Note that a script should prefer to return a <strong>typeSignatureRegistration</strong> object from its <strong>initializeScript</strong> method rather than doing this imperatively. Any script which makes changes imperatively is required to have an <strong>uninitializeScript</strong> method in order to clean up. An optional module name and version can restrict the registration. Versions are specified as "1.2.3.4" style strings.</td>
</tr>
</tbody>
</table>

**Diagnostics Functionality**

The diagnostics sub-namespace of the host object contains the following.

| Name     | Signature           | Phase Present | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------|---------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| debugLog | debugLog(object...) | 1             | This provides printf style debugging to a script extension. At present, output from debugLog is routed to the output console of the debugger. At a later point in time, there are plans to provide flexibility on routing this output. NOTE: This should not be used as a means of printing user output to console. It may not be routed there in the future. |

**Memory Functionality**

The memory sub-namespace of the host object contains the following.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Signature</th>
<th align="left">Phase Present</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">readMemoryValues</td>
<td align="left"><p>readMemoryValues(location, numElements, [elementSize], [isSigned], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a raw array of values from the address space of the debug target and places a typed array on top of the view of this memory. The supplied location can be an address (a 64-bit value), a location object, or a native pointer. The size of the array is indicated by the <em>numElements</em> argument. The size (and type) of each element of the array is given by the optional <em>elementSize</em> and <em>isSigned</em> arguments. If no such arguments are supplied, the default is byte (unsigned / 1 byte). If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger's current context. Note that using this method on 8, 16, and 32-bit values results in a fast typed view being placed over the read memory. Using this method on 64-bit values results in an array of 64-bit library types being constructed which is significantly more expensive!</td>
</tr>
<tr class="even">
<td align="left">readString</td>
<td align="left"><p>readString(location, [contextInheritor])</p>
<p>readString(location, [length], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a narrow (current code page) string from the address space of a debug target, converts it to UTF-16, and returns the result as a JavaScript string. It may throw an exception if the memory could not be read. The supplied location can be an address (a 64-bit value), a location object, or a native char<em>. If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger's current context. If the optional <em>length</em> argument is supplied, the read string will be of the specified length.</td>
</tr>
<tr class="odd">
<td align="left">readWideString</td>
<td align="left"><p>readWideString(location, [contextInheritor])</p>
<p>readWideString(location, [length], [contextInheritor])</p></td>
<td align="left">2</td>
<td align="left">This reads a wide(UTF-16) string from the address space of a debug target and returns the result as a JavaScript string. It may throw an exception if the memory could not be read. The supplied location can be an address (a 64-bit value), a location object, or a native wchar_t</em>. If the optional <em>contextInheritor</em> argument is supplied, memory will be read in the context (e.g.: address space and debug target) indicated by the argument; otherwise, it will be read from the debugger's current context. If the optional <em>length</em> argument is supplied, the read string will be of the specified length.</td>
</tr>
</tbody>
</table>

## <span id="Data-Model"></span><span id="data-model"></span><span id="DATA-MODEL"></span>Data Model Concepts in JavaScript

**Data Model Mapping**

The following data model concepts map to JavaScript.

| Concept                 | Native Interface             | JavaScript Equivalent                                                |
|-------------------------|------------------------------|----------------------------------------------------------------------|
| String Conversion       | IStringDisplayableConcept    | standard: toString(...){...}                                         |
| Iterability             | IIterableConcept             | standard: \[Symbol.iterator\](){...}                                 |
| Indexability            | IIndexableConcept            | protocol: getDimensionality(...) / getValueAt(...) / setValueAt(...) |
| Runtime Type Conversion | IPreferredRuntimeTypeConcept | protocol: getPreferredRuntimeTypedObject(...)                        |

**String Conversion**

The string conversion concept (IStringDisplayableConcept) directly translates to the standard JavaScript **toString** method. As all JavaScript objects have a string conversion (provided by Object.prototype if not provided elsewhere), every JavaScript object returned to the data model can be converted to a display string. Overriding the string conversion simply requires implementing your own toString.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IStringDisplayableConcept::ToDisplayString(...)
    //
    toString()
    { 
        return "This is my own string conversion!";
    }
}
```

**Iterability**

The data model's concept of whether an object is iterable or not maps directly to the ES6 protocol of whether an object is iterable. Any object which has a \[Symbol.iterator\] method is considered iterable. Implementation of such will make the object iterable.

An object which is only iterable can have an implementation such as follows.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIterableConcept::GetIterator
    //
    *[Symbol.iterator]()
    {
        yield "First Value";
        yield "Second Value";
        yield "Third Value";
    }
}
```

Special consideration must be given for objects which are both iterable and indexable as the objects returned from the iterator must include the index as well as the value via a special return type.

**Iterable and Indexable**

An object which is iterable and indexable requires a special return value from the iterator. Instead of yielding the values, the iterator yields instances of indexedValue. The indicies are passed as an array in the second argument to the indexedValue constructor. They can be multi-dimensional but must match the dimensionality returned in the indexer protocol.

This code shows an example implementaion.

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIterableConcept::GetIterator
    //
    *[Symbol.iterator]()
    {
        //
        // Consider this a map which mapped 42->"First Value", 99->"Second Value", and 107->"Third Value"
        //
        yield new host.indexedValue("First Value", [42]);
        yield new host.indexedValue("Second Value", [99]);
        yield new host.indexedValue("Third Value", [107]);
    }
}
```

**Indexability**

Unlike JavaScript, the data model makes a very explicit differentiation between property access and indexing. Any JavaScript object which wishes to present itself as indexable in the data model must implement a protocol consisting of a getDimensionality method which returns the dimensionality of the indexer and an optional pair of getValueAt and setValueAt methods which perform reads and writes of the object at supplied indicies. It is acceptable to omit either the getValueAt or setValueAt methods if the object is read-only or write-only

```javascript
class myObject
{
    //
    // This method will be called whenever any native code calls IIndexableConcept::GetDimensionality or IIterableConcept::GetDefaultIndexDimensionality
    //
    getDimensionality()
    {
        //
        // Pretend we are a two dimensional array.
        //
        return 2;
    } 

    //
    // This method will be called whenever any native code calls IIndexableConcept::GetAt
    //
    getValueAt(row, column)
    {
        return this.__values[row * this.__columnCount + column];
    }

    //
    // This method will be called whenever any native code calls IIndexableConcept::SetAt
    //
    setValueAt(value, row, column)
    {
        this.__values[row * this.__columnCount + column] = value;
    }
}
```

**Runtime Type Conversion**

This is only relevant for JavaScript prototypes/classes which are registered against type system (native) types. The debugger is often capable of performing analysis (e.g. Run-Time Type Information (RTTI) / v-table analysis) to determine the true runtime type of an object from a static type expressed in code. A data model registered against a native type can override this behavior via an implementation of the IPreferredRuntimeTypeConcept. Likewise, a JavaScript class or prototype registered against a native object can provide its own implementation via implementation of a protocol consisting of the getPreferredRuntimeTypedObject method.

Note that while this method can technically return anything, it is considered bad form for it to return something which isn't really the runtime type or a derived type. Such can result in significant confusion for users of the debugger. Overriding this method can, however, be valuable for things such as C-style header+object styles of implementation, etc...

```javascript
class myNativeModel
{
    //
    // This method will be called whenever the data model calls IPreferredRuntimeTypeConcept::CastToPreferredRuntimeType
    //
    getPreferredRuntimeTypedObject()
    {
        var loc = this.targetLocation;

        //
        // Perform analysis...
        //
        var runtimeLoc = loc.Add(runtimeObjectOffset);
  
        return host.createTypedObject(runtimeLoc, runtimeModule, runtimeTypeName);
    }
}
```

## <span id="related_topics"></span>Related topics

[Native Debugger Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

[Native Debugger Objects in JavaScript Extensions - Design and Testing Considerations](native-objects-in-javascript-extensions-design-considerations.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)
