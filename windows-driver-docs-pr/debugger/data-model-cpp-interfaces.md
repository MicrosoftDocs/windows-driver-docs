---
title: Debugger Data Model C++ Interfaces
description: This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.author: domars
ms.date: 04/06/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Data Model C++ Interfaces

This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

This page is part of a series on which describes the interfaces accessible from C++, how to use them to build a C++ based
debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.


Theses section in this topic introduce the the following.

[Overview of Debugger Data Model C++ Interfaces](#overview)

[Summary of Debugger Data Model Interfaces](#summary)

[The Core Debugger Object Model](#core)

[The Core Debugger Object Model - IModelObject](#imodelobject)

[Debugger Data Model C++ Host Interfaces](#hostinterface)

[Object Enumeration in the Data Model](#object)

[Debugger Data Model Host](#modelhost)

[Debugger Data Model Core Object Types](#objecttypes)

[Debugger Data Model System Interfaces](#systeminterfaces)

[Debugger Data Model Metadata Interfaces](#metadatainterfaces)



## <span id="Overview"> Overview of Debugger Debugger Data Model C++ Interfaces

The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's newer (dx) expression evaluator as well as from JavaScript extensions or other C++ extensions for that matter. 



## <span id="summary"> Summary of Debugger Data Model Interfaces

There are a multitude of C++ interfaces which comprise different pieces of the data model. In order to approach these interfaces in a consistent and easy manner, they are broken down by general category. The main areas here: 

**The General Object Model**

The first and most important set of interfaces define how to get access to the core data model and how to access and manipulate objects. IModelObject is the interface which represents every object in the data model (much like C#'s object). This is the main interface of interest for both consumers of and producers to the data model. The other interfaces are mechanisms for accessing different aspects of objects. 
The following interfaces are defined for this category: 


*Bridges Between DbgEng and the Data Model*

[IHostDataModelAccess]() 

*Main Interfaces* 

[IModelObject]() 

[IKeyStore]() 

[IModelIterator]() 

[IModelPropertyAccessor]() 

[IModelMethod]() 

[IKeyEnumerator]() 

[IRawEnumerator]() 

[IModelKeyReference]()  / [IModelKeyReference2]() 

*Concept Interfaces*

[IStringDisplayableConcept]() 

[IIterableConcept]() 

[IIndexableConcept]() 

[IPreferredRuntimeTypeConcept]() 

[IDataModelConcept]() 

[IDynamicKeyProviderConcept]() 

[IDynamicConceptProviderConcept]() 


**Management of Data Models and Extensibility**

The Data Model Manager is the core component which manages how all extensibility occurs. It is the central repository of a set of tables which map both native types to extension points as well as synthetic constructs to extension points. In addition, it is the entity which is responsible for the boxing of objects (conversion of ordinal values or strings into IModelObject's). 

The following interfaces are defined for this category: 

*General Data Model Manager Access* 

[IDataModelManager]()  / [IDataModelManager2]() 

*Script Management* 

[IDataModelScriptManager]() 

[IDataModelScriptProviderEnumerator]() 


**Access to the Debugger's Type System and Memory Spaces**

The underlying type system and memory spaces of the debugger are exposed in detail for extensions to make use of. 
The following interfaces are defined for this category: 

*General Host (Debugger) Interfaces*

[IDebugHost]() 

[IDebugHostStatus]() 

[IDebugHostContext]() 

[IDebugHostMemory]()  / [IDebugHostMemory2]() 

[IDebugHostErrorSink]() 

[IDebugHostEvaluator]()  / [IDebugHostEvaluator2]() 

[IDebugHostExtensibility]() 

*Host (Debugger) Type System Interfaces* 

[IDebugHostSymbols]() 

[IDebugHostSymbol]()  / IDebugHostSymbol2]() 

[IDebugHostModule]() 

[IDebugHostType]()  / IDebugHostType2]() 

[IDebugHostConstant]() 

[IDebugHostField]() 

[IDebugHostData]() 

[IDebugHostBaseClass]() 

[IDebugHostPublic]() 

[IDebugHostModuleSignature]() 

[IDebugHostTypeSignature]() 

*Host (Debugger) Support for Scripting* 

[IDebugHostScriptHost]() 


**Authoring and Consuming Scripts**

The Data Model also has a general notion of what a script is and how to debug one. It is entirely possible for a debugger extension to come along and define a general bridge between the data model and another dynamic language (usually a scripting environment). This set of interfaces is how that is accomplished as well as how a debugger UI can make use of such scripts. 

The following interfaces are defined for this category: 

*General Script Interfaces* 

[IDataModelScriptProvider]() 

[IDataModelScript]() 

[IDataModelScriptClient]() 

[IDataModelScriptHostContext]() 

[IDataModelScriptTemplate]() 

[IDataModelScriptTemplateEnumerator]() 

[IDataModelNameBinder]() 


*Script Debugger Interfaces* 

[IDataModelScriptDebug]() 

[IDataModelScriptDebugClient]() 

[IDataModelScriptDebugStack]() 

[IDataModelScriptDebugStackFrame]() 

[IDataModelScriptDebugVariableSetEnumerator]() 

[IDataModelScriptDebugBreakpoint]() 

[IDataModelScriptDebugBreakpointEnumerator]() 



## <span id="core">  The Core Debugger Object Model

One of the most basic yet powerful things about the data model is that it standardizes the definition of what an object is and how one
interacts with an object. The *IModelObject* interface encapsulates the notion of an object -- whether that object is an integer, a floating
point value, a string, some complex type in the target address space of the debugger, or some debugger concept like the notion of a process or a
module.

There are several different things that can be held in (or boxed into) an *IModelObject*:

-   **Intrinsic Values** - An *IModelObject* can be a container for a number of basic types: 8, 16, 32, or 64 bit signed or unsigned
    integers, booleans, strings, errors, or the notion of empty.

-   **Native Objects** - An *IModelObject* can represent a complex type (as defined by the debugger's type system) within the address space
    of whatever the debugger is targeting 
    
-   **Synthetic Objects** - An *IModelObject* can be a dynamic object --
    a dictionary if you will: a collection of key / value / metadata
    tuples and a set of **concepts** which define behaviors that aren't
    simply represented by key / value pairs.

-   **Properties** - An *IModelObject* can represent a property:
    something whose value can be retrieved or altered with a method call. A property within an *IModelObject* is effectively an *IModelPropertyAccessor* interface boxed into an *IModelObject*

-   **Methods** - An *IModelObject* can represent a method: something you can call with a set of arguments and get a return value. A
    method within an *IModelObject* is effectively an *IModelMethod* interface boxed into an *IModelObject*

### Extensibility Within The Object Model

An *IModelObject* is not an object in isolation. In addition to representing one of the types of objects shown above, each object has
the notion of a chain of parent data models. This chain behaves much like a [JavaScript prototype
chain](https://developer.mozilla.org/docs/Web/JavaScript/Inheritance_and_the_prototype_chain).
Instead of a linear chain of prototypes like JavaScript has, each data model object defines a linear chain of **parent models**. Each of those
parent models in turn has another linear chain of its own set of parents. In essence, each object is an aggregation of the capabilities
(properties, etc...) of both itself and every object in this tree. When a specific property is queried, if the object it is queried on does not
support that property, the query is passed in linear order to each parent in turn. This creates a behavior where the search for a property
is resolved by a depth-first search of the aggregate tree.

Extensibility within this object model is very simple given this notion that every object is an aggregate of itself and the tree of parent
models. An extension can come in and add itself into the list of parent models for another object. Doing this **extends** the object. In this
manner, it is possible to add capabilities onto anything: a particular instance of an object or value, a native type, the debugger's concept of
what a process or thread is, or even the notion of "all iterable objects".

### Context, Context, and Context: The **this** Pointer, The Address Space, and Implementation Private Data

There are three notions of **context** which are necessary to understand
within the context of the object model.

#### Context: The **this** Pointer

Since a given property or method may be implemented at any level of the
data model tree, it is necessary for the implementation of the method or
property to be able to access the original object (what you might call
the **this** pointer in C++ or the **this** object in JavaScript. That
instance object is passed to a variety of methods as the first argument
called **context** in the methods described.

#### Context: The Address Space

It is important to note that unlike prior extension models where
**context** (the target, process, thread you are looking at) is a UI
concept with all APIs relative to the current UI state, data model
interfaces typically take this context either explicitly or implicitly
as an *IDebugHostContext* interface. Each *IModelObject* within the data
model carries this type of context information along with it and can
propagate that context to objects it returns. This means that when you
read a native value or a key value out of an *IModelObject*, it will
read out of the target and process where the object was originally
acquired from.

There is an explicit constant value, **USE\_CURRENT\_HOST\_CONTEXT**,
that can be passed to methods which take an *IDebugHostContext*
argument. This value indicates that the context should indeed be the
current UI state of the debugger. This notion does, however, need to be
explicit.

#### Context: Implementation Private Data

Remember that each object in the data model is actually an aggregate of
the object instance and the tree of parent models which are attached.
Each of those parent models (which can be linked in the chains of many
different objects) can associate private implementation data with any
instance object. Each *IModelObject* which is created conceptually has a
hash table that maps from a particular parent model to private instance
data defined by an *IUnknown* interface. This allows a parent model to
cache information on every instance or have otherwise arbitrary data
associated.

This type of context is accessed through the *GetContextForDataModel*
and *SetContextForDataModel* methods on *IModelObject*.






## <span id="imodelobject"></span> The Core Debugger Object Interface: **IModelObject**

-------------------------------------------

The *IModelObject* interface is defined as follows:

```

DECLARE_INTERFACE_(IModelObject, IUnknown)\
{\
    STDMETHOD(QueryInterface)(_In_ REFIID iid, _COM_Outptr_ PVOID* iface);\
    STDMETHOD_(ULONG, AddRef)();\
    STDMETHOD_(ULONG, Release)() PURE;\
    STDMETHOD(GetContext)(_COM_Outptr_result_maybenull_ IDebugHostContext** context) PURE;\
    STDMETHOD(GetKind)(_Out_ ModelObjectKind *kind) PURE;\
    STDMETHOD(GetIntrinsicValue)(_Out_ VARIANT* intrinsicData);\
    STDMETHOD(GetIntrinsicValueAs)(_In_ VARTYPE vt, _Out_ VARIANT* intrinsicData) PURE;\
    STDMETHOD(GetKeyValue)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;\
    STDMETHOD(SetKeyValue)(_In_ PCWSTR key, _In_opt_ IModelObject* object) PURE;\
    STDMETHOD(EnumerateKeyValues)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;\
    STDMETHOD(GetRawValue)(_In_ SymbolKind kind, _In_ PCWSTR name, _In_ ULONG searchFlags, _COM_Errorptr_ IModelObject** object) PURE;\
    STDMETHOD(EnumerateRawValues)(_In_ SymbolKind kind, _In_ ULONG searchFlags, _COM_Outptr_ IRawEnumerator** enumerator) PURE;\
    STDMETHOD(Dereference)(_COM_Errorptr_ IModelObject** object) PURE;\
    STDMETHOD(TryCastToRuntimeType)(_COM_Errorptr_ IModelObject** runtimeTypedObject) PURE;\
    STDMETHOD(GetConcept)(_In_ REFIID conceptId, _COM_Outptr_ IUnknown** conceptInterface, _COM_Outptr_opt_result_maybenull_ IKeyStore** conceptMetadata) PURE;\
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;\
    STDMETHOD(GetTypeInfo)(_Out_ IDebugHostType** type) PURE;\
    STDMETHOD(GetTargetInfo)(_Out_ Location* location, _Out_ IDebugHostType** type) PURE;\
    STDMETHOD(GetNumberOfParentModels)(_Out_ ULONG64* numModels) PURE;\
    STDMETHOD(GetParentModel)(_In_ ULONG64 i, _COM_Outptr_ IModelObject **model, _COM_Outptr_result_maybenull_ IModelObject **contextObject) PURE;\
    STDMETHOD(AddParentModel)(_In_ IModelObject* model, _In_opt_ IModelObject* contextObject, _In_ bool override) PURE;\
    STDMETHOD(RemoveParentModel)(_In_ IModelObject* model) PURE;\
    STDMETHOD(GetKey)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;\
    STDMETHOD(GetKeyReference)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** objectReference, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;\
    STDMETHOD(SetKey)(_In_ PCWSTR key, _In_opt_ IModelObject* object, _In_opt_ IKeyStore* metadata) PURE;\
    STDMETHOD(ClearKeys)() PURE;\
    STDMETHOD(EnumerateKeys)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;\
    STDMETHOD(EnumerateKeyReferences)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;\
    STDMETHOD(SetConcept)(_In_ REFIID conceptId, _In_ IUnknown* conceptInterface, _In_opt_ IKeyStore* conceptMetadata) PURE;\
    STDMETHOD(ClearConcepts)() PURE;\
    STDMETHOD(GetRawReference)(_In_ SymbolKind kind, _In_ PCWSTR name, _In_ ULONG searchFlags, _COM_Errorptr_ IModelObject** object) PURE;\
    STDMETHOD(EnumerateRawReferences)(_In_ SymbolKind kind, _In_ ULONG searchFlags, _COM_Outptr_ IRawEnumerator** enumerator) PURE;\
    STDMETHOD(SetContextForDataModel)(_In_ IModelObject* dataModelObject, _In_ IUnknown* context) PURE;\
    STDMETHOD(GetContextForDataModel)(_In_ IModelObject* dataModelObject, _Out_ IUnknown** context) PURE;\
    STDMETHOD(Compare)(_In_ IModelObject* other, _COM_Outptr_opt_result_maybenull_ IModelObject **ppResult) PURE;\
    STDMETHOD(IsEqualTo)(_In_ IModelObject* other, _Out_ bool* equal) PURE;\
}
```

**Basic Methods**

The following are general methods applicable to any kind of object represented by an IModelObject. 

```
STDMETHOD(GetKind)(_Out_ ModelObjectKind *kind) PURE;
STDMETHOD(GetContext)(_COM_Outptr_result_maybenull_ IDebugHostContext** context) PURE;
STDMETHOD(GetIntrinsicValue)(_Out_ VARIANT* intrinsicData);
STDMETHOD(GetIntrinsicValueAs)(_In_ VARTYPE vt, _Out_ VARIANT* intrinsicData) PURE;
STDMETHOD(Compare)(_In_ IModelObject* other, _COM_Outptr_opt_result_maybenull_ IModelObject **ppResult) PURE;
STDMETHOD(IsEqualTo)(_In_ IModelObject* other, _Out_ bool* equal) PURE;
STDMETHOD(Dereference)(_COM_Errorptr_ IModelObject** object) PURE;
```

[GetKind]() 

The GetKind method returns what kind of object is boxed inside the IModelObject. 

[GetContext]()

The GetContext method returns the host context that is associated with the object. 

[GetIntrinsicValue]()

The GetIntrinsicValue method returns the thing which is boxed inside an IModelObject. This method may only legally be called on IModelObject interfaces which represent a boxed intrinsic or a particular interface which is boxed. It cannot be called on native objects, no value objects, synthetic objects, and reference objects. The GetIntrinsicValueAs method behaves much as the GetIntrinsicValue method excepting that it converts the value to the specified variant type. If the conversion cannot be performed, the method returns an error.

[IsEqualTo]()

The IsEqualTo method compares two model objects and returns whether they are equal in value. For object which have an ordering, this method returning true is equivalent to the Compare method returning 0. For objects that have no ordering but are equatable, the Compare method will fail, but this will not. The meaning of a value based comparison is defined by the type of object. At present, this is only defined for intrinsic types and error objects. There is no current data model concept for equatability. 

[Dereference]()

The Dereference method dereferences an object. This method can be used to dereference a data model based reference (ObjectTargetObjectReference, ObjectKeyReference) or a native language reference (a pointer or a language reference). It is important to note that this method removes a single level of reference semantics on the object. It is entirely possible to, for instance, have a data model reference to a language reference. In such a case, calling the Dereference method the first time would remove the data model reference and leave the language reference. Calling Dereference on that resulting object would subsequently remove the language reference and return the native value under that reference. 


**Key Manipulation Methods**

Any synthetic object which is a dictionary of key, value, and metadata tuples has a series of methods to manipulate those keys, values, and the metadata associated with them. 

The value based forms of the APIs are: 
```
STDMETHOD(GetKeyValue)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
STDMETHOD(SetKeyValue)(_In_ PCWSTR key, _In_opt_ IModelObject* object) PURE;
STDMETHOD(EnumerateKeyValues)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;
The key based forms of the APIs (including those used for key creation) are: 
STDMETHOD(GetKey)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
STDMETHOD(SetKey)(_In_ PCWSTR key, _In_opt_ IModelObject* object, _In_opt_ IKeyStore* metadata) PURE;
STDMETHOD(EnumerateKeys)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;
STDMETHOD(ClearKeys)() PURE;
```
The reference based forms of the APIs are: 

```
STDMETHOD(GetKeyReference)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** objectReference, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
STDMETHOD(EnumerateKeyReferences)(_COM_Outptr_ IKeyEnumerator** enumerator) PURE;
```
[GetKeyValue]()

The GetKeyValue method is the first method a client will turn to in order to get the value of (and the metadata associated with) a given key by name. If the key is a property accessor -- that is it's value as an IModelObject which is a boxed IModelPropertyAccessor, the GetKeyValue method will automatically call the property accessor's GetValue method in order to retrieve the actual value.

[SetKeyValue]()

The SetKeyValue method is the first method a client will turn to in order to set the value of a key. This method cannot be used to create a new key on an object. It will only set the value of an existing key. Note that many keys are read-only (e.g.: they are implemented by a property accessor which returns E_NOT_IMPL from it's SetValue method). This method will fail when called on a read only key. 

[EnumerateKeyValues]()

The EnumerateKeyValues method is the first method a client will turn to in order to enumerate all of the keys on an object (this includes all keys implemented anywhere in the tree of parent models). It is important to note that EnumerateKeyValues will enumerate any keys defined by duplicate names in the object tree; however -- methods like GetKeyValue and SetKeyValue will only manipulate the first instance of a key with the given name as discovered by the depth-first-traversal. 

[GetKey]()

The GetKey method will get the value of (and the metadata associated with) a given key by name. Most clients should utilize the GetKeyValue method instead. If the key is a property accessor, calling this method will return the property accessor (an IModelPropertyAccessor interface) boxed into an IModelObject. Unlike, GetKeyValue, this method will not automatically resolve the underlying value of the key by calling the GetValue method. That responsibility is the caller's. 

[SetKey]()

The SetKey method is the method a client will turn to in order to create a key on an object (and potentially associate metadata with the created key). If a given object already has a key with the given name, one of two behaviors will occur. If the key is on the instance given by this, the value of that key will be replaced as if the original key did not exist. If, on the other hand, the key is in the chain of parent data models of the instance given by this, a new key with the given name will be created on the instance given by this. This would, in effect, cause the object to have two keys of the same name (similar to a derived class shadowing a member of the same name as a base class). 

[EnumerateKeys]()

The EnumerateKeys method behaves similar to the EnumerateKeyValues method excepting that it does not automatically resolve property accessors on the object. This means that if the value of a key is a property accessor, the EnumerateKeys method will return the property accessor (an IModelPropertyAccessorInterface) boxed into an IModelObject rather than automatically calling the GetValue method. This is similar to the difference between GetKey and GetKeyValue. 

[ClearKeys]()

The ClearKeys method removes all keys and their associated values and metadata from the instance of the object specified by this. This method has no effect on parent models attached to the particular object instance. 

[GetKeyReference]()

The GetKeyReference method will search for a key of the given name on the object (or its parent model chain) and return a reference to that key given by an IModelKeyReference interface boxed into an IModelObject. That reference can subsequently be used to get or set the value of the key. 

[EnumerateKeyReferences]()

The EnumerateKeyReferences method behaves similar to the EnumerateKeyValues method excepting that it returns references to the keys it enumerates (given by an IModelKeyReference interface boxed into an IModelObject) instead of the value of the key. Such references can be used to get or set the underlying value of the keys. 


**Concept Manipulation Methods**

In addition to a model object being a dictionary of key/value/metadata tuples, it is also a container of concepts. A concept is something abstract that can be performed on or by an object. Concepts are, in essence, a dynamic store of interfaces that an object supports. A number of concepts are defined by the data model today: 

Concept Interface | Description
------------------|-------------
IDataModelConcept | The concept is a parent model. If this model is automatically attached to a native type via a registered type signature, the InitializeObject method will automatically be called every time a new object of such type is instantiated.
IStringDisplayableConcept  | The object can be converted to a string for display purposes.
IIterableConcept  | The object is a container and can be iterated.
IIndexableConcept  | The object is a container and can be indexed (accessed via random access) in one or more dimensions.
IPreferredRuntimeTypeConcept  | The object understands more about types derived from it than the underlying type system is capable of providing and would like to handle its own conversions from static to runtime type.
IDynamicKeyProviderConcept | The object is a dynamic provider of keys and wishes to take over all key queries from the core data model. This interface is typically used as a bridge to dynamic languages such as JavaScript.
IDynamicConceptProviderConcept  | The object is a dynamic provider of concepts and wishes to take over all concept queries from the core data model. This interface is typically used as a bridge to dynamic languages such as JavaScript.

The following methods on IModelObject are utilized to manipulate the concepts that an object supports. 

```
STDMETHOD(GetConcept)(_In_ REFIID conceptId, _COM_Outptr_ IUnknown** conceptInterface, _COM_Outptr_opt_result_maybenull_ IKeyStore** conceptMetadata) PURE;
STDMETHOD(SetConcept)(_In_ REFIID conceptId, _In_ IUnknown* conceptInterface, _In_opt_ IKeyStore* conceptMetadata) PURE;
STDMETHOD(ClearConcepts)() PURE;
```
[GetConcept]()

The GetConcept method will search for a concept on the object (or its parent model chain) and return an interface pointer to the concept interface. The behavior and methods on a concept interface are specific to each concept. It is important to note, however, that many of the concept interfaces require the caller to explicitly pass the context object (or what one might traditionally call the this pointer). It is important to ensure that the correct context object is passed to every concept interface.

[SetConcept]()

The SetConcept method will place a specified concept on the object instance specified by the this pointer. If a parent model attached to the object instance specified by this also supports the concept, the implementation in the instance will override that in the parent model. 

[ClearConcepts]()

The ClearConcepts method will remove all concepts from the instance of the object specified by this. 


**Native Object Methods**

While many model objects refer to intrinsics (e.g.: integers, strings) or synthetic constructs (a dictionary of key/value/metadata tuples and concepts), a model object may also refer to a native construct (e.g.: a user defined type in the address space of the debug target). The IModelObject interface has a series of methods on it which access information about such native objects. Those methods are: 

```
STDMETHOD(GetRawValue)(_In_ SymbolKind kind, _In_ PCWSTR name, _In_ ULONG searchFlags, _COM_Errorptr_ IModelObject** object) PURE;
STDMETHOD(EnumerateRawValues)(_In_ SymbolKind kind, _In_ ULONG searchFlags, _COM_Outptr_ IRawEnumerator** enumerator) PURE;
STDMETHOD(TryCastToRuntimeType)(_COM_Errorptr_ IModelObject** runtimeTypedObject) PURE;
STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
STDMETHOD(GetTypeInfo)(_Out_ IDebugHostType** type) PURE;
STDMETHOD(GetTargetInfo)(_Out_ Location* location, _Out_ IDebugHostType** type) PURE;
STDMETHOD(GetRawReference)(_In_ SymbolKind kind, _In_ PCWSTR name, _In_ ULONG searchFlags, _COM_Errorptr_ IModelObject** object) PURE;
STDMETHOD(EnumerateRawReferences)(_In_ SymbolKind kind, _In_ ULONG searchFlags, _COM_Outptr_ IRawEnumerator** enumerator) PURE;
```

[GetRawValue]()

The GetRawValue method finds a native construct within the given object. Such a construct may be a field, a base class, a field in a base class, a member function, etc... 

[EnumerateRawValues]()

The EnumerateRawValues method enumerates all native children (e.g.: fields, base classes, etc...) of the given object. 


[TryCastToRuntimeType]()

The TryCastToRuntimeType method will ask the debug host to perform an analysis and determine the actual runtime type (e.g.: most derived class) of the given object. The exact analysis utilized is specific to the debug host and may include RTTI (C++ run time type information), examination of the V-Table(virtual function table) structure of the object, or any other means that the host can use to reliably determine dynamic/runtime type from the static type. Failure to convert to a runtime type does not mean that this method call will fail. In such cases, the method will return the given object (the this pointer) in the output argument. 

[GetLocation]() 

The GetLocation method will return the location of the native object. While such a location is typically a virtual address within the address space of the debug target, it is not necessarily so. The location returned by this method is an abstract location that may be a virtual address, may indicate placement within a register or sub-register, or may indicate some other arbitrary address space as defined by the debug host. If the HostDefined field of the resulting Location object is 0, it indicates that the location is actually a virtual address. Such virtual address may be retrieved by examining the Offset field of the resulting location. Any non-zero value of the HostDefined field indicates an alternate address space where the Offset field is the offset within that address space. The exact meaning of non-zero HostDefined values here are private to the debug host. 

[GetTypeInfo]()

The GetTypeInfo method will return the native type of the given object. If the object does not have native type information associated with it (e.g.: it is an intrinsic, etc...), the call will still succeed but will return null. 

[GetTargetInfo]()

The GetTargetInfo method is effectively a combination of the GetLocation and GetTypeInfo methods returning both the abstract location as well as native type of the given object. 

[GetRawReference]()

The GetRawReference method finds a native construct within the given object and returns a reference to it. Such a construct may be a field, a base class, a field in a base class, a member function, etc... It is important to distinguish the reference returned here (an object of the type ObjectTargetObjectReference) from a language reference (e.g.: a C++ & or && style reference). 

[EnumerateRawReferences]()

The EnumerateRawReferences method enumerates references to all native children (e.g.: fields, base classes, etc...) of the given object. 


**Extensibility Methods**

As described earlier, a model object behaves very similar to a JavaScript object and its prototype chain. In addition to the instance represented by a given IModelObject interface, there may be an arbitrary number of parent models attached to the object (each of which may, in turn, have an arbitrary number of parent models attached to them). This is the primary means for extensibility within the data model. If a given property or concept cannot be located within a given instance, a depth-first search of the object tree (defined by parent models) rooted at the instance is performed. 

The following methods manipulate the chain of parent models associated with a given IModelObject instance: 

```
STDMETHOD(GetNumberOfParentModels)(_Out_ ULONG64* numModels) PURE;
STDMETHOD(GetParentModel)(_In_ ULONG64 i, _COM_Outptr_ IModelObject **model, _COM_Outptr_result_maybenull_ IModelObject **contextObject) PURE;
STDMETHOD(AddParentModel)(_In_ IModelObject* model, _In_opt_ IModelObject* contextObject, _In_ bool override) PURE;
STDMETHOD(RemoveParentModel)(_In_ IModelObject* model) PURE;
STDMETHOD(SetContextForDataModel)(_In_ IModelObject* dataModelObject, _In_ IUnknown* context) PURE;
STDMETHOD(GetContextForDataModel)(_In_ IModelObject* dataModelObject, _Out_ IUnknown** context) PURE;
```

[GetNumberOfParentModels]()

The GetNumberOfParentModels method returns the number of parent models which are attached to the given object instance. Parent models are searched for properties depth-first in the linear ordering of the parent model chain. 

[GetParentModel]()

The GetParentModel method returns the i-th parent model in the parent model chain of the given object. Parent models are searched for a property or concept in the linear order they are added or enumerated. The parent model with index i of zero is searched (hierarchically) before the parent model with index i + 1. 

[AddParentModel]()

The AddParentModel method adds a new parent model to the given object. Such a model may be added at the end of the search chain (the override argument is specified as false) or at the front of the search chain (the override argument is specified as true). In addition, each parent model may optionally adjust the context (the semantic this pointer) for any property or concept on the given parent (or anyone in its parent hierarchy). Context adjustment is seldom used but allows for some powerful concepts like object embedding, constructing namespaces, etc... 

[RemoveParentModel]()

The RemoveParentModel will remove a specified parent model from the parent search chain of the given object. 

[SetContextForDataModel]()

The SetContextForDataModel method is used by the implementation of a data model to place implementation data on instance objects. Conceptually, each IModelObject (call this the instance for simplicity) contains a hash table of state. The hash table is indexed by another IModelObject (call this the data model for simplicity) which is in the parent model hierarchy of the instance. The value contained in this hash is a set of reference counted state information represented by an IUnknown instance. Once the data model sets this state on the instance it can store arbitrary implementation data which can be retrieved during things like property getters. 

[GetContextForDataModel]()

The GetContextForDataModel method is used to retrieve context information which was set up with a prior call to SetContextForDataModel. This retrieves state information which was set on an instance object by a data model further up in the instance object's parent model hierarchy. 
For more details about this context/state and its meaning, see the documentation for SetContextForDataModel. 



## <span id="hostinterface"></span> Debugger Data Model C++ Host Interfaces

**The Debugger Data Model Host**

The Debugger Data Model is designed to be a componentized system which can be hosted in a variety of different contexts. Normally, the Data Model is hosted in the context of a debugger application. In order to be a host of the data model, a number of interfaces need to be implemented to expose core aspects of the debugger: its targeting, its memory spaces, its evaluator, its symbolic and type system, etc... While these interfaces are implemented by any application wishing to host the data model, they are consumed by both the core data model as well as any extension which interoperates with the data model. 

The set of core interfaces are: 

Interface Name | Description
|--------------|---------------|
IDebugHost | The core interface to the debug host.
IDebugHostStatus  | An interface allowing a client to query for the status of the host.
IDebugHostContext  | An abstraction of a context within the host (e.g.: a particular target, a particular process, a particular address space, etc...)
IDebugHostErrorSink  | An interface implemented by callers to receive errors from certain portions of the host and data model
IDebugHostEvaluator / IDebugHostEvaluator2  | The debug host's expression evaluator.
IDebugHostExtensibility  | An interface for extending the capabilities of the host or portions of it (such as the expression evaluator).

The type system and symbolic interfaces are: 

InterfaceName | Description
|--------------|---------------|
IDebugHostSymbols | Core interface which provides access to and resolution of symbols
IDebugHostSymbol / IDebugHostSymbol2  | Represents a single symbol of any kind. The particular symbol is a derivation of this interface.
IDebugHostModule | Represents a module loaded within a process. This is a kind of symbol.
IDebugHostType / IDebugHostType2  | Represents a native/language type.
IDebugHostConstant  | Represents a constant within symbolic information (e.g.: a non-type template argument in C++)
IDebugHostField  | Represents a field within a structure or class.
IDebugHostData | Represents data within a module (were this within a structure or class it would be an IDebugHostField)
IDebugHostBaseClass
Represents a base class.
IDebugHostPublic  | Represents a symbol within the publics table of a PDB. This does not have type information associated with it. It is a name and address.
IDebugHostModuleSignature | Represents a module signature -- a definition which will match a set of modules by name and/or version
IDebugHostTypeSignature | Represents a type signature -- a definition which will match a set of types by module and/or name


**The Core Host Interface: IDebugHost**

The IDebugHost interface is the core interface of any data model host. It is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHost, IUnknown)
{
    STDMETHOD(GetHostDefinedInterface)(_COM_Outptr_ IUnknown** hostUnk) PURE;
    STDMETHOD(GetCurrentContext)(_COM_Outptr_ IDebugHostContext** context) PURE;
    STDMETHOD(GetDefaultMetadata)(_COM_Outptr_ IKeyStore** defaultMetadataStore) PURE;
}
```

**GetHostDefinedInterface**

The GetHostDefinedInterface method returns the host's main private interface, if such exists for the given host. For Debugging Tools for Windows, the interface returned here is an IDebugClient (cast to IUnknown). 

[GetCurrentContext]()

The GetCurrentContext method returns an interface which represents the current state of the debugger host. The exact meaning of this is left up to the host, but it typically includes things such as the session, process, and address space that is active in the user interface of the debug host. The returned context object is largely opaque to the caller but it is an important object to pass between calls to the debug host. When a caller is, for instance, reading memory, it is important to know which process and address space that memory is being read from. That notion is encapsulated in the notion of the context object which is returned from this method. 

[GetDefaultMetadata]()

The GetDefaultMetadata method returns a default metadata store that may be used for certain operations (e.g.: string conversion) when no explicit metadata has been passed. This allows the debug host to have some control over the way some data is presented. For example, the default metadata may include a PreferredRadix key, allowing the host to indicate whether ordinals should be displayed in decimal or hexadecimal if not otherwise specified. 

Note that property values on the default metadata store must be manually resolved and must pass the object for which the default metadata is being queried. The GetKey method should be used in lieu of GetKeyValue. 

**The Status Interface:** 

[IDebugHostStatus]()

The IDebugHostStatus interface allows a client of the data model or the debug host to inquire about certain aspects of the debug host's status. T

[PollUserInterrupt]()

The PollUserInterrupt method is used to inquire whether the user of the debug host has requested an interruption of the current operation. A property accessor in the data model may, for instance, call into arbitrary code (e.g.: a JavaScript method). That code may take an arbitrary amount of time. In order to keep the debug host responsive, any such code which may take an arbitrary amount of time should check for an interrupt request via calling this method. If the interruptRequested value comes back as true, the caller should immediately abort and return a result of E_ABORT. 


**The Context Interface: IDebugHostContext**

Context is one of the most important aspects of the data model and the underlying debug host. When you hold an object, it is important to be able to know where an object came from -- what process is it in, what address space is it associated with. Knowing this information allows the correct interpretation of things like pointer values. 
An object of the type IDebugHostContext must be passed to many methods on the debug host. This interface can be acquired in a number of ways: 
By getting the current context of the debugger: calling the GetCurrentContext method of IDebugHost
By getting the context of an object: calling the GetContext method of IModelObject
By getting the context of a symbol: calling the GetContext method of IDebugHostSymbol
In addition, there are two values which have special meaning in the context of an IDebugHostContext interface which is either returned from or passed to a data model or debug host method: 
nullptr: an indication that there is no context. It is perfectly valid for some objects to have no context. The Debugger object in the root namespace of the data model does not refer to anything within a specific process or address space. It has no context.
USE_CURRENT_HOST_CONTEXT: a sentinel value indicating that one should use the current UI context of the debug host. This value will never be returned from the debug host. It may, however, be passed to any debug host method which takes an input IDebugHostContext in lieu of explicitly calling the GetCurrentContext method of IDebugHost. Note that explicitly passing USE_CURRENT_HOST_CONTEXT is often more performant than explicitly getting the current context. 
The contexts of a host context are largely opaque to the caller. The only operation that a caller outside the core debug host can do with a host context is to compare it to another host context. 

The IDebugHostContext interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostContext, IUnknown)
{
    STDMETHOD(IsEqualTo)(_In_ IDebugHostContext *pContext, _Out_ bool *pIsEqual) PURE;
}
```

[IsEqualTo]()

The IsEqualTo method compares a host context to another host context. If the two contexts are equivalent, an indication of this is returned. Note that this comparison is not interface equivalence. This compares the underlying opaque contents of the context itself. 

[The Error Sink: IDebugHostErrorSink]()

The IDebugHostErrorSink is a means by which a client can receive notifications of errors which occur during certain operations and route those errors where needed. 

[ReportError]()

The ReportError method is a callback on the error sink to notify it that an error has occurred and allow the sink to route the error to whatever UI or mechanism is appropriate. 

[The Host Evaluator: IDebugHostEvaluator / IDebugHostEvaluator2]()

One of the most important pieces of functionality which the debug host provides to clients is access to its language based expression evaluator. The IDebugHostEvaluator and IDebugHostEvaluator2 interfaces are the means to access that functionality from the debug host. 

[EvaluateExpression]()

The EvaluateExpression method allows requests the debug host to evaluate a language (e.g.: C++) expression and return the resulting value of that expression evaluation boxed as an IModelObject. This particular variant of the method only allows language constructs. Any additional functionality which is presented within the expression evaluator of the debug host that is not present in the language (e.g.: LINQ query methods) is turned off for the evaluation. 

[EvaluateExtendedExpression]()

The EvaluateExtendedExpression method is similar to the EvaluateExpression method except that it turns back on additional non-language functionality which a particular debug host chooses to add to its expression evaluator. For Debugging Tools for Windows, for example, this enables anonymous types, LINQ queries, module qualifiers, format specifiers, and other non-C/C++ functionality. 


**IDebugHostEvaluator2 AssignTo**

The AssignTo method performs assignment according to the semantics of the language being debugged. 

The Host Extensibility Interface: IDebugHostExtensibility]()
Certain functionality of the debug host is optionally subject to extensibility. This may, for instance, include the expression evaluator. The IDebugHostExtensibility interface is the means by which these extensibility points are accessed. 
The interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostExtensibility, IUnknown)
{
    STDMETHOD(CreateFunctionAlias)(_In_ PCWSTR aliasName, _In_ IModelObject *functionObject) PURE;
    STDMETHOD(DestroyFunctionAlias)(_In_ PCWSTR aliasName) PURE;
}
```

[CreateFunctionAlias]()

The CreateFunctionAlias method creates a "function alias", a "quick alias" for a method implemented in some extension. The meaning of this alias is host specific. It may extend the host's expression evaluator with the function or it may do something entirely different. 

[DestroyFunctionAlias]()

The DestroyFunctionAlias method undoes a prior call to the CreateFunctionAlias method. The function will no longer be available under the quick alias name. 



## <span id="object"></span> Object Enumeration in the Data Model

**Enumerating Objects in the Data Model**

There are two core key enumeration interfaces in the data model: IKeyEnumerator and IRawEnumerator. While these are the two core interfaces, they can be used to enumerate objects in one of three styles: 

*Keys* - The IKeyEnumerator interface can be acquired via a call to EnumerateKeys in order to enumerate the keys of an object and their values/metadata without resolving any underlying property accessors. This style of enumeration can return raw IModelPropertyAccessor values boxed into IModelObjects.

*Values* - The IKeyEnumerator and IRawEnumerator interfaces can be acquired via calls to either EnumerateKeyValues or EnumerateRawValues in order to enumerate the keys/raw values on an object and their values/metadata. Any property accessors present in the enumeration are automatically resolved via a call to the underlying GetValue method during such an enumeration.

*References* - The IKeyEnumerator and IRawEnumerator interfaces can be acquired via calls to either EnumerateKeyReferences or EnumerateRawReferences in order to enumerate references to the keys/raw values on an object. Such references can be saved and later used to get or set the underlying key or raw value.

**KeyEnumerator: Enumeration of synthetic keys**

The IKeyEnumerator interface is the single interface for the enumeration of all keys (by key, value, or reference) within an instance object and all the associated parent models in its parent model chain. The interface is defined as follows: 

```
DECLARE_INTERFACE_(IKeyEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_Out_ BSTR* key, _COM_Errorptr_opt_ IModelObject** value, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
}
```

[Reset]()

The Reset method resets the enumerator to the position it was at when it was first acquired (e.g.: before the first element in the enumeration). A subsequent call to GetNext will return the first enumerated key. 

[GetNext]()

The GetNext method both moves the enumerator forward and returns the key at that position in the enumeration.


**IRawEnumerator: Enumeration of native or underlying language (C/C++) constructs**

The IRawEnumerator interface is the single interface for the enumeration of all native/language constructs (by value or reference) within a object which represents a native construct within the address space of the debug target. 
The interface is defined as follows: 

```
DECLARE_INTERFACE_(IRawEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_Out_opt_ BSTR* name, _Out_opt_ SymbolKind *kind, _COM_Errorptr_opt_ IModelObject** value) PURE;
}
```

[Reset]()

The Reset method resets the enumerator to the position it was at when it was first acquired (e.g.: before the first element in the enumeration). A subsequent call to GetNext will return the first enumerated native/language construct. 

[GetNext]()

The GetNext method both moves the enumerator forward and returns the native/language construct at that position in the enumeration. 



## <span id="modelhost"></span> The Debugger Data Model Host


The Debugger Data Model is designed to be a componentized system which can be hosted in a variety of different contexts. Normally, the Data Model is hosted in the context of a debugger application. In order to be a host of the data model, a number of interfaces need to be implemented to expose core aspects of the debugger: its targeting, its memory spaces, its evaluator, its symbolic and type system, etc... While these interfaces are implemented by any application wishing to host the data model, they are consumed by both the core data model as well as any extension which interoperates with the data model. 

The set of core interfaces are: 

Interface Name | Description
|--------------|------------------|
IDebugHost | The core interface to the debug host.
IDebugHostStatus  | An interface allowing a client to query for the status of the host.
IDebugHostContext  | An abstraction of a context within the host (e.g.: a particular target, a particular process, a particular address space, etc...)
IDebugHostErrorSink  | An interface implemented by callers to receive errors from certain portions of the host and data model
IDebugHostEvaluator / IDebugHostEvaluator2  | The debug host's expression evaluator.
IDebugHostExtensibility  | An interface for extending the capabilities of the host or portions of it (such as the expression evaluator).

The [type system and symbolic interfaces]() are: 

Interface Name | Description
|--------------|------------------|
IDebugHostSymbols | Core interface which provides access to and resolution of symbols
IDebugHostSymbol / IDebugHostSymbol2 | Represents a single symbol of any kind. The particular symbol is a derivation of this interface.
IDebugHostModule | Represents a module loaded within a process. This is a kind of symbol.
IDebugHostType / IDebugHostType2 | Represents a native/language type.
IDebugHostConstant | Represents a constant within symbolic information (e.g.: a non-type template argument in C++)
IDebugHostField | Represents a field within a structure or class.
IDebugHostData | Represents data within a module (were this within a structure or class it would be an IDebugHostField)
IDebugHostBaseClass | Represents a base class.
IDebugHostPublic | Represents a symbol within the publics table of a PDB. This does not have type information associated with it. It is a name and address.
IDebugHostModuleSignature | Represents a module signature -- a definition which will match a set of modules by name and/or version
IDebugHostTypeSignature | Represents a type signature -- a definition which will match a set of types by module and/or name


**The Core Host Interface: *IDebugHost***

The IDebugHost interface is the core interface of any data model host. It is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHost, IUnknown)
{
    STDMETHOD(GetHostDefinedInterface)(_COM_Outptr_ IUnknown** hostUnk) PURE;
    STDMETHOD(GetCurrentContext)(_COM_Outptr_ IDebugHostContext** context) PURE;
    STDMETHOD(GetDefaultMetadata)(_COM_Outptr_ IKeyStore** defaultMetadataStore) PURE;
}
```

[GetHostDefinedInterface]()

The GetHostDefinedInterface method returns the host's main private interface, if such exists for the given host. For Debugging Tools for Windows, the interface returned here is an IDebugClient (cast to IUnknown). 

[GetCurrentContext]()

The GetCurrentContext method returns an interface which represents the current state of the debugger host. The exact meaning of this is left up to the host, but it typically includes things such as the session, process, and address space that is active in the user interface of the debug host. The returned context object is largely opaque to the caller but it is an important object to pass between calls to the debug host. When a caller is, for instance, reading memory, it is important to know which process and address space that memory is being read from. That notion is encapsulated in the notion of the context object which is returned from this method. 

[GetDefaultMetadata]()

The GetDefaultMetadata method returns a default metadata store that may be used for certain operations (e.g.: string conversion) when no explicit metadata has been passed. This allows the debug host to have some control over the way some data is presented. For example, the default metadata may include a PreferredRadix key, allowing the host to indicate whether ordinals should be displayed in decimal or hexadecimal if not otherwise specified. 
Note that property values on the default metadata store must be manually resolved and must pass the object for which the default metadata is being queried. The GetKey method should be used in lieu of GetKeyValue. 


**The Status Interface: *IDebugHostStatus***

The IDebugHostStatus interface allows a client of the data model or the debug host to inquire about certain aspects of the debug host's status. 

The interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostStatus, IUnknown)
{
    STDMETHOD(PollUserInterrupt)(_Out_ bool* interruptRequested) PURE;
}
```

[PollUserInterrupt]()

The PollUserInterrupt method is used to inquire whether the user of the debug host has requested an interruption of the current operation. A property accessor in the data model may, for instance, call into arbitrary code (e.g.: a JavaScript method). That code may take an arbitrary amount of time. In order to keep the debug host responsive, any such code which may take an arbitrary amount of time should check for an interrupt request via calling this method. If the interruptRequested value comes back as true, the caller should immediately abort and return a result of E_ABORT. 


**The Context Interface: *IDebugHostContext*** 

Context is one of the most important aspects of the data model and the underlying debug host. When you hold an object, it is important to be able to know where an object came from -- what process is it in, what address space is it associated with. Knowing this information allows the correct interpretation of things like pointer values. 

An object of the type IDebugHostContext must be passed to many methods on the debug host. This interface can be acquired in a number of ways: 
By getting the current context of the debugger: calling the GetCurrentContext method of IDebugHost
By getting the context of an object: calling the GetContext method of IModelObject
By getting the context of a symbol: calling the GetContext method of IDebugHostSymbol

In addition, there are two values which have special meaning in the context of an IDebugHostContext interface which is either returned from or passed to a data model or debug host method: 
nullptr: an indication that there is no context. It is perfectly valid for some objects to have no context. The Debugger object in the root namespace of the data model does not refer to anything within a specific process or address space. It has no context.
USE_CURRENT_HOST_CONTEXT: a sentinel value indicating that one should use the current UI context of the debug host. This value will never be returned from the debug host. It may, however, be passed to any debug host method which takes an input IDebugHostContext in lieu of explicitly calling the GetCurrentContext method of IDebugHost. Note that explicitly passing USE_CURRENT_HOST_CONTEXT is often more performant than explicitly getting the current context. 

The contexts of a host context are largely opaque to the caller. The only operation that a caller outside the core debug host can do with a host context is to compare it to another host context. 

The IDebugHostContext interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostContext, IUnknown)
{
    STDMETHOD(IsEqualTo)(_In_ IDebugHostContext *pContext, _Out_ bool *pIsEqual) PURE;
}
```

[IsEqualTo]()
The IsEqualTo method compares a host context to another host context. If the two contexts are equivalent, an indication of this is returned. Note that this comparison is not interface equivalence. This compares the underlying opaque contents of the context itself. 
It is also important to note that this method checks for equivalence and not that one of the contexts is a subset or superset of the other. 


**The Error Sink: *IDebugHostErrorSink*** 

The IDebugHostErrorSink is a means by which a client can receive notifications of errors which occur during certain operations and route those errors where needed.

[ReportError]()

The ReportError method is a callback on the error sink to notify it that an error has occurred and allow the sink to route the error to whatever UI or mechanism is appropriate. 


**The Host Evaluator: *IDebugHostEvaluator / IDebugHostEvaluator2*** 

One of the most important pieces of functionality which the debug host provides to clients is access to its language based expression evaluator. The IDebugHostEvaluator and IDebugHostEvaluator2 interfaces are the means to access that functionality from the debug host. 


The interfaces are defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostEvaluator2, IDebugHostEvaluator)
{
    //
    // IDebugHostEvaluator:
    //
    STDMETHOD(EvaluateExpression)(_In_ IDebugHostContext* context, _In_ PCWSTR expression, _In_opt_ IModelObject* bindingContext, _COM_Errorptr_ IModelObject** result, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    STDMETHOD(EvaluateExtendedExpression)(_In_ IDebugHostContext* context, _In_ PCWSTR expression, _In_opt_ IModelObject* bindingContext, _COM_Errorptr_ IModelObject** result, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    //
    // IDebugHostEvaluator2:
    //
    STDMETHOD(AssignTo)(_In_ IModelObject* assignmentReference, _In_ IModelObject* assignmentValue, _COM_Errorptr_ IModelObject** assignmentResult, _COM_Outptr_opt_result_maybenull_ IKeyStore** assignmentMetadata) PURE;
}
```

[EvaluateExpression]()

The EvaluateExpression method allows requests the debug host to evaluate a language (e.g.: C++) expression and return the resulting value of that expression evaluation boxed as an IModelObject. This particular variant of the method only allows language constructs. Any additional functionality which is presented within the expression evaluator of the debug host that is not present in the language (e.g.: LINQ query methods) is turned off for the evaluation. 

[EvaluateExtendedExpression]()

The EvaluateExtendedExpression method is similar to the EvaluateExpression method except that it turns back on additional non-language functionality which a particular debug host chooses to add to its expression evaluator. For Debugging Tools for Windows, for example, this enables anonymous types, LINQ queries, module qualifiers, format specifiers, and other non-C/C++ functionality. 

[IDebugHostEvaluator2 AssignTo]()

The AssignTo method performs assignment according to the semantics of the language being debugged. 


**The Host Extensibility Interface: *IDebugHostExtensibility*** 

Certain functionality of the debug host is optionally subject to extensibility. This may, for instance, include the expression evaluator. The IDebugHostExtensibility interface is the means by which these extensibility points are accessed. 

The interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostExtensibility, IUnknown)
{
    STDMETHOD(CreateFunctionAlias)(_In_ PCWSTR aliasName, _In_ IModelObject *functionObject) PURE;
    STDMETHOD(DestroyFunctionAlias)(_In_ PCWSTR aliasName) PURE;
}
```

[CreateFunctionAlias]()

The CreateFunctionAlias method creates a "function alias", a "quick alias" for a method implemented in some extension. The meaning of this alias is host specific. It may extend the host's expression evaluator with the function or it may do something entirely different. 

[DestroyFunctionAlias]()

The DestroyFunctionAlias method undoes a prior call to the CreateFunctionAlias method. The function will no longer be available under the quick alias name. 


## <span id="objecttypes"></span> Debugger Data Model Core Object Types


An object in the data model is similar to the notion of Object in .NET. It is the generic container into which construct that the data model understands can be boxed. In addition to native objects and synthetic (dynamic) objects, there are a series of core object types which can be placed (or boxed) into the container of an IModelObject. The container in which most of these values are placed is a standard COM/OLE VARIANT with a number of additional restrictions placed upon what that VARIANT can contain. The most basic types of these are:

- 8-bit unsigned and signed values (VT_UI1, VT_I1)
- 16-bit unsigned and signed values (VT_UI2, VT_UI2)
- 32-bit unsigned and signed values (VT_UI4, VT_I4)
- 64-bit unsigned and signed values (VT_UI8, VT_I8)
- Single and double precision floating point values (VT_R4, VT_R8)
- Strings (VT_BSTR)
- Booleans (VT_BOOL)

In addition to these basic types, a number of core data model objects are placed into IModelObject defined by VT_UNKNOWN where the stored IUnknown is guaranteed to implement a specific interface. These types are: 

- Property accessors (IModelPropertyAccessor)
- Method objects (IModelMethod)
- Key reference objects (IModelKeyReference or IModelKeyReference2)
- Context objects (IDebugModelHostContext)

**Property Accessors *(IModelPropertyAccessor)***

A property accessor in the data model is an implementation of the IModelPropertyAccessor interface which is boxed into an IModelObject. The model object will return a kind of ObjectPropertyAccessor when queried and the intrinsic value is a VT_UNKNOWN which is guaranteed to be queryable for IModelPropertyAccessor. In process, it is guaranteed to be statically castable to IModelPropertyAccessor. 

A property accessor is an indirect way to get a method call for getting and setting a key value in the data model. If a given key's value is a property accessor, the GetKeyValue and SetKeyValue methods will automatically notice this and call the property accessor's underlying GetValue or SetValue methods as appropriate. 

The IModelPropertyAccessor interface is defined as follows: 

```
DECLARE_INTERFACE_(IModelPropertyAccessor, IUnknown)
{
    STDMETHOD(GetValue)(_In_ PCWSTR key, _In_opt_ IModelObject* contextObject, _COM_Outptr_ IModelObject** value) PURE;
    STDMETHOD(SetValue)(_In_ PCWSTR key, _In_opt_ IModelObject* contextObject, _In_ IModelObject* value) PURE; 
}
```

[GetValue]()

The GetValue method is the getter for the property accessor. It is called whenever a client wishes to fetch the underlying value of the property. Note that any caller which directly gets a property accessor is responsible for passing the key name and accurate instance object (this pointer) to the property accessor's GetValue method. 

[SetValue]()

The SetValue method is the setter for the property accessor. It is called whenever a client wishes to assign a value to the underlying property. Many properties are read-only. In such cases, calling the SetValue method will return E_NOTIMPL. Note that any caller which directly gets a property accessor is responsible for passing the key name and accurate instance object (this pointer) to the property accessor's SetValue method. 


**Methods *(IModelMethod)***

A method in the data model is an implementation of the IModelMethod interface which is boxed into an IModelObject. The model object will return a kind of ObjectMethod when queried and the intrinsic value is a VT_UNKNOWN which is guaranteed to be queryable for IModelMethod. In process, it is guaranteed to be statically castable to IModelMethod. 
All methods in the data model are dynamic in nature. They take as input a set of 0 or more arguments and return a single output value. There is no overload resolution and no metadata about parameter names, types, or expectations. 

The IModelMethod interface is defined as follows: 

```
DECLARE_INTERFACE_(IModelMethod, IUnknown)
{
    STDMETHOD(Call)(_In_opt_ IModelObject *pContextObject, _In_ ULONG64 argCount, _In_reads_(argCount) IModelObject **ppArguments, _COM_Errorptr_ IModelObject **ppResult, _COM_Outptr_opt_result_maybenull_ IKeyStore **ppMetadata) PURE;
}
```

[Call]()

The Call method is the way in which any method defined in the data model is invoked. The caller is responsible for passing an accurate instance object (this pointer) and an arbitrary set of arguments. The result of the method and any optional metadata associated with that result is returned. Methods which do not logically return a value still must return a valid IModelObject. In such a case, the IModelObject is a boxed no value. In the event a method fails, it may return optional extended error information in the input argument (even if the returned HRESULT is a failure). It is imperative that callers check for this. 


**Key References *(IModelKeyReference or IModelKeyReference2)***

A key reference is, in essence, a handle to a key on a particular object. A client can retrieve such handle via methods such as GetKeyReference and use the handle later to get or set the value of the key without necessarily holding onto the original object. This type of object is an implementation of the IModelKeyReference or IModelKeyReference2 interface which is boxed into an IModelObject. The model object will return a kind of ObjectKeyReference when queried and then intrinsic value is a VT_UNKNOWN which is guaranteed to be queryable for IModelKeyReference. In process, it is guaranteed to be statically castable to IModelKeyReference. 

The key reference interface is defined as follows: 

```
DECLARE_INTERFACE_(IModelKeyReference2, IModelKeyReference)
{
    STDMETHOD(GetKeyName)(_Out_ BSTR* keyName) PURE;
    STDMETHOD(GetOriginalObject)(_COM_Outptr_ IModelObject** originalObject) PURE;
    STDMETHOD(GetContextObject)(_COM_Outptr_ IModelObject** containingObject) PURE;
    STDMETHOD(GetKey)(_COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    STDMETHOD(GetKeyValue)(_COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    STDMETHOD(SetKey)(_In_opt_ IModelObject* object, _In_opt_ IKeyStore* metadata) PURE;
    STDMETHOD(SetKeyValue)(_In_ IModelObject* object) PURE;
    STDMETHOD(OverrideContextObject)(_In_ IModelObject* newContextObject) PURE;
}
```

[GetKeyName]()

The GetKeyName method returns the name of the key to which this key reference is a handle. The returned string is a standard BSTR and must be freed via a call to SysFreeString. 

[GetOriginalObject]()

The GetOriginalObject method returns the instance object from which the key reference was created. Note that the key may itself be on a parent model of the instance object. 

[GetContextObject]()

The GetContextObject method returns the context (this pointer) which will be passed to a property accessor's GetValue or SetValue method if the key in question refers to a property accessor. The context object returned here may or may not be the same as the original object fetched from GetOriginalObject. If a key is on a parent model and there is a context adjustor associated with that parent model, the original object is the instance object on which GetKeyReference or EnumerateKeyReferences was called. The context object would be whatever comes out of the final context adjustor between the original object and the parent model containing the key to which this key reference is a handle. If there are no context adjustors, the original object and the context object are identical. 

[GetKey]()

The GetKey method on a key reference behaves as the GetKey method on IModelObject would. It returns the value of the underlying key and any metadata associated with the key. If the value of the key happens to be a property accessor, this will return the property accessor (IModelPropertyAccessor) boxed into an IModelObject. This method will not call the underlying GetValue or SetValue methods on the property accessor. 

[GetKeyValue]()

The GetKeyValue method on a key reference behaves as the GetKeyValue method on IModelObject would. It returns the value of the underlying key and any metadata associated with the key. If the value of the key happens to be a property accessor, this will call the underlying GetValue method on the property accessor automatically. 


[SetKey]()

The SetKey method on a key reference behaves as the SetKey method on IModelObject would. It will assign the value of the key. If the original key was a property accessor, this will replace the property accessor. It will not call the SetValue method on the property accessor. 


[SetKeyValue]()

The SetKeyValue method on a key reference behaves as the SetKeyValue method on IModelObject would. It will assign the value of the key. If the original key was a property accessor, this will call the underlying SetValue method on the property accessor rather than replacing the property accessor itself. 

[OverrideContextObject]()

The OverrideContextObject method (only present on IModelKeyReference2) is an advanced method which is used to permanently alter the context object which this key reference will pass to any underlying property accessor's GetValue or SetValue methods. The object passed to this method will also be returned from a call to GetContextObject. This method can be used by script providers to replicate certain dynamic language behaviors. Most clients should not call this method. 


**Context Objects *(IDebugHostContext)***

Context objects are opaque blobs of information that the debug host (in cooperation with the data model) associates with every object. It may include things such as the process context or address space the information comes from, etc... A context object is an implementation of IDebugHostContext boxed within an IModelObject. Note that IDebugHostContext is a host defined interface. A client will never implement this interface. 

For more information about context objects, see [Debugger Data Model C++ Host Interfaces](#hostinterface), in this topic. 



## <span id="systeminterfaces"></span> Debugger Data Model System Interfaces

**The Data Model Host**

The Debugger Data Model is designed to be a componentized system which can be hosted in a variety of different contexts. Normally, the Data Model is hosted in the context of a debugger application. In order to be a host of the data model, a number of interfaces need to be implemented to expose core aspects of the debugger: its targeting, its memory spaces, its evaluator, its symbolic and type system, etc... While these interfaces are implemented by any application wishing to host the data model, they are consumed by both the core data model as well as any extension which interoperates with the data model. 

The type system and symbolic interfaces are: 


Interface Name | Description
|--------------|------------------|
IDebugHostSymbols  | Core interface which provides access to and resolution of symbols
IDebugHostSymbol / IDebugHostSymbol2  | Represents a single symbol of any kind. The particular symbol is a derivation of this interface.
IDebugHostModule  | Represents a module loaded within a process. This is a kind of symbol.
IDebugHostType / IDebugHostType2  | Represents a native/language type.
IDebugHostConstant  | Represents a constant within symbolic information (e.g.: a non-type template argument in C++)
IDebugHostField | Represents a field within a structure or class.
IDebugHostData | Represents data within a module (were this within a structure or class it would be an IDebugHostField)
IDebugHostBaseClass  | Represents a base class.
IDebugHostPublic | Represents a symbol within the publics table of a PDB. This does not have type information associated with it. It is a name and address.
IDebugHostModuleSignature | Represents a module signature -- a definition which will match a set of modules by name and/or version
IDebugHostTypeSignature | Represents a type signature -- a definition which will match a set of types by module and/or name

The other core interfaces are: 

Interface Name | Description
|--------------|------------------|
IDebugHost | The core interface to the debug host.
IDebugHostStatus | An interface allowing a client to query for the status of the host.
IDebugHostContext | An abstraction of a context within the host (e.g.: a particular target, a particular process, a particular address space, etc...)
IDebugHostErrorSink | An interface implemented by callers to receive errors from certain portions of the host and data model
IDebugHostEvaluator / IDebugHostEvaluator2 | The debug host's expression evaluator.
IDebugHostExtensibility | An interface for extending the capabilities of the host or portions of it (such as the expression evaluator).


**The Main Symbolic Interface: *IDebugHostSymbols***

The IDebugHostSymbols interface is the main starting point to access symbols in the debug target. This interface can be queried from an instance of IDebugHost and is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostSymbols, IUnknown)
{
    STDMETHOD(CreateModuleSignature)(_In_z_ PCWSTR pwszModuleName, _In_opt_z_ PCWSTR pwszMinVersion, _In_opt_z_ PCWSTR pwszMaxVersion, _Out_ IDebugHostModuleSignature** ppModuleSignature) PURE;
    STDMETHOD(CreateTypeSignature)(_In_z_ PCWSTR signatureSpecification, _In_opt_ IDebugHostModule* module, _Out_ IDebugHostTypeSignature** typeSignature) PURE;
    STDMETHOD(CreateTypeSignatureForModuleRange)(_In_z_ PCWSTR signatureSpecification, _In_z_ PCWSTR moduleName, _In_opt_z_ PCWSTR minVersion, _In_opt_z_ PCWSTR maxVersion, _Out_ IDebugHostTypeSignature** typeSignature) PURE;
    STDMETHOD(EnumerateModules)(_In_ IDebugHostContext* context, _COM_Outptr_ IDebugHostSymbolEnumerator** moduleEnum) PURE;
    STDMETHOD(FindModuleByName)(_In_ IDebugHostContext* context, _In_z_ PCWSTR moduleName, _COM_Outptr_ IDebugHostModule **module) PURE;
    STDMETHOD(FindModuleByLocation)(_In_ IDebugHostContext* context, _In_ Location moduleLocation, _COM_Outptr_ IDebugHostModule **module) PURE;
    STDMETHOD(GetMostDerivedObject)(_In_opt_ IDebugHostContext *pContext, _In_ Location location, _In_ IDebugHostType* objectType, _Out_ Location* derivedLocation, _Out_ IDebugHostType** derivedType) PURE;
}
```

CreateModuleSignature]()

The CreateModuleSignature method creates a signature which can be used to match a set of specific modules by name and optionally, by version. 
There are three components to a module signature: 

- A name: a matching module must have a name which is an exact case insensitive match against the name in the signature
- A minimum version: if specified, a matching module must have a minimum version which is at least as high as this version. Versions are specified in "A.B.C.D" format with each subsequent portion being less important than the prior. Only the first segment is mandatory.
- A maximum version: if specified, a matching module must have a maximum version which is no higher than this version. Versions are specified in "A.B.C.D" format with each subsequent portion being less important than the prior. Only the first segment is mandatory.

[CreateTypeSignature]()

The CreateTypeSignature method creates a signature which can be used to match a set of concrete types by containing module and type name. The format of the type name signature string is specific to the language being debugged (and debug host). For C/C++, the signature string is equivalent to a NatVis Type Specification. That is, the signature string is a type name where wildcards (specified as *) are allowed for template arguments. 

[CreateTypeSignatureForModuleRange]()

The CreateTypeSignatureForModuleRange method creates a signature which can be used to match a set of concrete types by module signature and type name. This is similar to the CreateTypeSignature method excepting that instead of passing a specific module to match for the signature, the caller passes the arguments necessary to create a module signature (as if the module signature were created with the CreateModuleSignature method). 

[EnumerateModules]()

The EnumerateModules method creates an enumerator which will enumerate every module available in a particular host context. That host context might encapsulate a process context or it might encapsulate something like the Windows kernel. 


[FindModuleByName]()

The FindModuleByName method will look through the given host context and locate a module which has the specified name and return an interface to it. It is legal to search for the module by name with or without the file extension. 

[FindModuleByLocation]()

The FindModuleByLocation method will look through the given host context and determine what module contains the address given by the specified location. It will then return an interface to such module. 

[GetMostDerivedObject]()

The GetMostDerivedObject will use the type system of the debugger to determine the runtime type of an object from its static type. This method will only use symbolic information and heuristics available at the type system layer in order to perform this analysis. Such information may include C++ RTTI (run time type information) or analysis of the shape of the virtual function tables of the object. It does not include things such as the preferred runtime type concept on an IModelObject. 
If the analysis cannot find a runtime type or cannot find a runtime type different from the static type passed into the method, the input location and type may be passed out. The method will not fail for these reasons. 



**The Core Individual Symbol Interface: *IDebugHostSymbol***

Every symbol that can be returned from the data model host will derive in some fashion from IDebugHostSymbol. This is the core interface that every symbol implements regardless of the kind of symbol. Depending on the kind of symbol, a given symbol may implement a set of other interfaces which return attributes more unique to the particular kind of symbol represented by this interface. The IDebugHostSymbol2 / 
IDebugHostSymbol interface is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostSymbol2, IDebugHostSymbol)
{
    // 
    // IDebugHostSymbol:
    //
    STDMETHOD(GetContext)(_COM_Outptr_ IDebugHostContext** context) PURE;
    STDMETHOD(EnumerateChildren)(_In_ SymbolKind kind, _In_opt_z_ PCWSTR name, _Out_ IDebugHostSymbolEnumerator **ppEnum) PURE;
    STDMETHOD(GetSymbolKind)(_Out_ SymbolKind *kind) PURE;
    STDMETHOD(GetName)(_Out_ BSTR* symbolName) PURE;
    STDMETHOD(GetType)(_Out_ IDebugHostType** type) PURE;
    STDMETHOD(GetContainingModule)(_Out_ IDebugHostModule **containingModule) PURE;
    STDMETHOD(CompareAgainst)(_In_ IDebugHostSymbol *pComparisonSymbol, _In_ ULONG comparisonFlags, _Out_ bool *pMatches) PURE;
    //
    // IDebugHostSymbol2
    //
    STDMETHOD(EnumerateChildrenEx)(_In_ SymbolKind kind, _In_opt_z_ PCWSTR name, _In_opt_ SymbolSearchInfo* searchInfo, _Out_ IDebugHostSymbolEnumerator **ppEnum) PURE;
}
```

It is very important to note that this interface represents many kinds of symbols -- delineated by the SymbolKind enumeration which has values as follows: 

Enumarant | Meaning
|--------------|------------------|
Symbol  | Unspecified symbol type 
SymbolModule | The symbol is a module and can be queried for IDebugHostModule
SymbolType | The symbol is a type and can be queried for IDebugHostType
SymbolField | The symbol is a field (a data member within a structure or class) and can be queried for IDebugHostField
SymbolConstant | The symbol is a constant value and can be queried for IDebugHostConstant
SymbolData | The symbol is data which is not a member of a structure or class and is queryable for IDebugHostData
SymbolBaseClass | The symbol is a base class and is queryable for IDebugHostBaseClass
SymbolPublic | The symbol is an entry in a module's publics table (having no type information) and is queryable for IDebugHostPublic
SymbolFunction | The symbol is a function and is queryable for IDebugHostData

[GetContext]()

The GetContext method returns the context where the symbol is valid. While this will represent things such as the debug target and process/address space in which the symbol exists, it may not be as specific as a context retrieved from other means (e.g.: from an *IModelObject*). 

[EnumerateChildren]()

The EnumerateChildren method returns an enumerator which will enumerate all children of a given symbol. For a C++ type, for example, the base classes, fields, member functions, and the like are all considered children of the type symbol. 


**The Module Interface: *IDebugHostModule***

The debugger's notion of a module that is loaded within some address space is represented in two distinct ways in the data model: 
At the type system level via the IDebugHostModule interface. Here, a module is a symbol and core attributes of the module are interface method calls
Projected at the data model level via the Debugger.Models.Module data model. This is an extensible encapsulation of the type system IDebugHostModule representation of a module.

The IDebugHostModule interface is defined as follows (ignoring methods that are generic to IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostModule, IDebugHostSymbol)
{
    //
    // IDebugHostModule:
    //
    STDMETHOD(GetImageName)(_In_ bool allowPath, _Out_ BSTR* imageName) PURE;
    STDMETHOD(GetBaseLocation)(_Out_ Location* moduleBaseLocation) PURE;
    STDMETHOD(GetVersion)(_Out_opt_ ULONG64* fileVersion, _Out_opt_ ULONG64* productVersion) PURE;
    STDMETHOD(FindTypeByName)(_In_z_ PCWSTR typeName, _Out_ IDebugHostType** type) PURE;
    STDMETHOD(FindSymbolByRVA)(_In_ ULONG64 rva, _Out_ IDebugHostSymbol** symbol) PURE;
    STDMETHOD(FindSymbolByName)(_In_z_ PCWSTR symbolName, _Out_ IDebugHostSymbol** symbol) PURE;
}
```

[GetImageName]()

The GetImageName method returns the image name of the module. Depending on the value of the allowPath argument, the returned image name may or may not include the full path to the image.

[GetBaseLocation]()

The GetBaseLocation method returns the base load address of the module as a location structure. The returned location structure for a module will typically refer to a virtual address.

[GetVersion]()

The GetVersion method returns version information about the module (assuming that such information can successfully be read out of the headers). If a given version is requested (via a non-nullptr output pointer) and it cannot be read, an appropriate error code will be returned from the method call. 

[FindTypeByName]()

The FindTypeByName method finds a type defined within the module by the type name and returns a type symbol for it. This method may return a valid IDebugHostType which would never be returned via explicit recursion of children of the module. The debug host may allow creation of derivative types -- types not ever used within the module itself but derived from types that are. As an example, if the structure MyStruct is defined in the symbols of the module but the type MyStruct ** is never used, the FindTypeByName method may legitimately return a type symbol for MyStruct ** despite that type name never explicitly appearing in the symbols for the module. 

[FindSymbolByRVA]()

The FindSymbolByRVA method will find a single matching symbol at the given relative virtual address within the module. If there is not a single symbol at the supplied RVA (e.g.: there are multiple matches), an error will be returned by this method. Note that this method will prefer returning a private symbol over a symbol in the publics table. 

[FindSymbolByName]()

The FindSymbolByName method will find a single global symbol of the given name within the module. If there is not a single symbol matching the given name, an error will be returned by this method. Note that this method will prefer returning a private symbol over a symbol in the publics table. 

Access to the Type System: IDebugHostType2 / IDebugHostType]()

A given language/native type is described by the IDebugHostType2 or IDebugHostType interfaces. Note that some of the methods on these interfaces only apply for specific kinds of types. A given type symbol may refer to one of the following types as described by the TypeKind enumeration: 

Type Kind |  Description
|--------------|------------------|
TypeUDT | A user defined type (a struct, class, union, etc...). A model object which has a native type whose kind is TypeUDT has a canonical representation of ObjectTargetObject where the type is always kept inside the corresponding IModelObject.
TypePointer | A pointer. A model object which has a native type whose kind is TypePointer has a canonical representation of ObjectIntrinsic where the pointer's value is zero extended to VT_UI8 and kept as intrinsic data in this 64-bit form. Any type symbol of TypePointer has a base type (as returned by the GetBaseType method) of the type that the pointer points to.
TypeMemberPointer | A pointer to class member. A model object which has a native type whose kind is TypeMemberPointer has a canonical representation which is intrinsic (the value being the same as the pointer value). The exact meaning of this value is compiler/debug host specific.
TypeArray | An array. A model object which has a native type whose kind is TypeArray has a canonical representation of ObjectTargetObject. The base address of the array is the object's location (retrieved via the GetLocation method) and the type of the array is always kept. Any type symbol of TypeArray has a base type (as returned by the GetBaseType method) of the type that the array is an array of.
TypeFunction | A function.
TypeTypedef | A typedef. A model object which has a native type whose kind would otherwise be TypeTypedef has a canonical representation identical to the canonical representation of the final type underlying the typedef. This appears completely transparent to the end user of the object and the type information unless the explicit typedef methods of IDebugHostType2 are utilized to query typedef information or there is an explicit data model registered against the typedef. Note that the GetTypeKind method will never return TypeTypedef. Every method will return what the final type underlying the typedef would return. There are typedef specific methods on IDebugHostType2 which can be used to get the typedef specific information.
TypeEnum | An enum. A model object which has a native type whose kind is TypeEnum has a canonical representation of ObjectIntrinsic where the value and type of the intrinsic is identical to the enum value. 
TypeIntrinsic | An intrinsic (base type). A model object which has a native type whose kind is TypeIntrinsic has a canonical representation of ObjectIntrinsic. The type information may or may not be kept -- particularly if the underlying type is fully described by the variant data type (VT_*) of the intrinsic data stored in the IModelObject

The overall IDebugHostType2 / IDebugHostType interface is defined as follows (excluding IDebugHostSymbol methods): 

```
DECLARE_INTERFACE_(IDebugHostType2, IDebugHostType)
{
    //
    // IDebugHostType:
    //
    STDMETHOD(GetTypeKind)(_Out_ TypeKind *kind) PURE;
    STDMETHOD(GetSize)(_Out_ ULONG64* size) PURE;
    STDMETHOD(GetBaseType)(_Out_ IDebugHostType** baseType) PURE;
    STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
    STDMETHOD(GetIntrinsicType)(_Out_opt_ IntrinsicKind *intrinsicKind, _Out_opt_ VARTYPE *carrierType) PURE;
    STDMETHOD(GetBitField)(_Out_ ULONG* lsbOfField, _Out_ ULONG* lengthOfField) PURE;
    STDMETHOD(GetPointerKind)(_Out_ PointerKind* pointerKind) PURE;
    STDMETHOD(GetMemberType)(_Out_ IDebugHostType** memberType) PURE;
    STDMETHOD(CreatePointerTo)(_In_ PointerKind kind, _COM_Outptr_ IDebugHostType** newType) PURE;
    STDMETHOD(GetArrayDimensionality)(_Out_ ULONG64* arrayDimensionality) PURE;
    STDMETHOD(GetArrayDimensions)(_In_ ULONG64 dimensions, _Out_writes_(dimensions) ArrayDimension *pDimensions) PURE;
    STDMETHOD(CreateArrayOf)(_In_ ULONG64 dimensions, _In_reads_(dimensions) ArrayDimension *pDimensions, _COM_Outptr_ IDebugHostType** newType) PURE;
    STDMETHOD(GetFunctionCallingConvention)(_Out_ CallingConventionKind* conventionKind) PURE;
    STDMETHOD(GetFunctionReturnType)(_COM_Outptr_ IDebugHostType** returnType) PURE;
    STDMETHOD(GetFunctionParameterTypeCount)(_Out_ ULONG64* count) PURE;
    STDMETHOD(GetFunctionParameterTypeAt)(_In_ ULONG64 i, _Out_ IDebugHostType** parameterType) PURE;
    STDMETHOD(IsGeneric)(_Out_ bool* isGeneric) PURE;
    STDMETHOD(GetGenericArgumentCount)(_Out_ ULONG64* argCount) PURE;
    STDMETHOD(GetGenericArgumentAt)(_In_ ULONG64 i, _Out_ IDebugHostSymbol** argument) PURE;
    //
    // IDebugHostType2:
    //
    STDMETHOD(IsTypedef)(_Out_ bool* isTypedef) PURE;
    STDMETHOD(GetTypedefBaseType)(_Out_ IDebugHostType2** baseType) PURE;
    STDMETHOD(GetTypedefFinalBaseType)(_Out_ IDebugHostType2** finalBaseType) PURE;
    STDMETHOD(GetFunctionVarArgsKind)(_Out_ VarArgsKind* varArgsKind) PURE;
}
```

**IDebugHostType2/IDebugHostType General Methods**

The following IDebugHostType methods are general to any type regardless of what kind is returned from the GetTypeKind method: 

```
STDMETHOD(GetTypeKind)(_Out_ TypeKind *kind) PURE;
STDMETHOD(GetSize)(_Out_ ULONG64* size) PURE;
STDMETHOD(GetBaseType)(_Out_ IDebugHostType** baseType) PURE;
STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
```

[GetTypeKind]()

The GetTypeKind method returns what kind of type (pointer, array, intrinsic, etc...) the symbol refers to. 

[GetSize]()

The GetSize method returns the size of the type (as if one had done sizeof(type) in C++). 

[GetBaseType]()

If the type is a derivative of another single type (e.g.: as MyStruct * is derived from MyStruct'), the GetBaseType method returns the base type of the derivation. For pointers, this returns the type pointed to. For arrays, this returns what the array is an array of. If the type is not such a derivative type, an error is returned. 

[GetHashCode]()

The GetHashCode method returns a 32-bit hash code for the type. With the exception of a global match (e.g.: a type signature equivalent to * which matches everything if permitted by the host), any type instance which can match a particular type signature must return the same hash code. 
This method is used in conjunction with type signatures in order to match type signatures to type instances. 


**IDebugHostType2/IDebugHostType Intrinsic Methods**

The following IDebugHostType methods are specific to intrinsic types (or types which hold intrinsic data such as enums): 

```
STDMETHOD(GetIntrinsicType)(_Out_opt_ IntrinsicKind *intrinsicKind, _Out_opt_ VARTYPE *carrierType) PURE;
```

[GetIntrinsicType]()

The GetIntrinsicType method returns information about what kind of intrinsic the type is. Two values are returned out of this method: 

- The intrinsic kind indicates the overall type (e.g.: integer, unsigned, floating point) but not the size of the type (e.g.: 8 bit, 16 bit, 32 bit, 64 bit)
- The carrier type indicates how the intrinsic kind packs into a VARIANT structure. This is a VT_* constant.

The combination of the two values provides the full set of information about the intrinsic. 


**IDebugHostType2/IDebugHostType Bitfield Methods**

The following IDebugHostType methods are specific to types which store data in bitfields. Information about bitfield placement within an intrinsic is stored as part of the type symbol in the data model rather than being an attribute of the location. 

```
STDMETHOD(GetBitField)(_Out_ ULONG* lsbOfField, _Out_ ULONG* lengthOfField) PURE;
```

[GetBitField]()

If a given member of a data structure is a bitfield (e.g.: ULONG MyBits:8), the type information for the field carries with it information about the bitfield placement. The GetBitField method can be used to retrieve that information. This method will fail on any type which is not a bitfield. This is the only reason the method will fail. Simply calling this method and looking at success/failure is sufficient to distinguish a bit field from a non-bit field. 
If a given type does happen to be a bitfield, the field positions are defined by the half open set *(lsbOfField + lengthOfField : lsbOfField]*


**IDebugHostType2/IDebugHostType Pointer Related Methods**

The following IDebugHostType methods are specific to pointer types. Such are types where GetTypeKind returns TypePointer or TypeMemberPointer': 

```
STDMETHOD(GetPointerKind)(_Out_ PointerKind* pointerKind) PURE;
STDMETHOD(GetMemberType)(_Out_ IDebugHostType** memberType) PURE;
```
[GetPointerKind]()
For types which are pointers, the GetPointerKind method returns the kind of pointer. This is defined by the PointerKind enumeration.

[GetMemberType]()
For types which are pointer-to-member (as indicated by a type kind of TypeMemberPointer), the GetMemberType method returns the class the pointer is a pointer-to-member of. 

**IDebugHostType2/IDebugHostType Array Related Methods**

Arrays are types where GetTypeKind returns TypeArray. Note that arrays as defined by the debug host's type system are not the same as the single dimensional, zero index based, packed linear one dimensional arrays that C utilizes. C style arrays fit into the definition but the overall scope of an array is broader in IDebugHostType. 
An array in the debug host can be multi-dimensional and each dimension within the array is defined by a descriptor known as an ArrayDimensionThis descriptor has the following fields: 



Field | Meaning
|--------------|------------------|
LowerBound | The base index of the array as a signed 64-bit value. For a C style array, this will always be zero. It need not be. An individual dimension of an array can be considered to start at any 64-bit index, even a negative one.
Length | The length of the array dimension as an unsigned 64-bit value. The indicies of the array span the half open set [LowerBound, LowerBound + Length).
Stride | Defines the stride of the array dimension. For an increase of one (from N to N + 1) in the index of this dimension, this indicates how many bytes to move forward in memory. For a C style array, this would be the size of each element of the array. It does not need to be. Padding between elements can be expressed as a stride greater than the size of each individual element. For multi-dimensional arrays, this value would indicate how to move an entire dimension forward. Consider an M x N matrix. This might be described in row-major form as two dimensions: { [LowerBound: 0, Length: M, Stride: N \* sizeof(element)], [LowerBound: 0, Length: N, Stride: sizeof(element)]} or it might be alternatively be described in column-major form as two dimensions: { [LowerBound: 0, Length: M, Stride: sizeof(element)], [LowerBound: 0, Length: N, Stride: M \* sizeof(element)]} The ArrayDimension concept allows this degree of flexibility. The following IDebugHostType methods are specific to array types. STDMETHOD(GetArrayDimensionality)(\_Out_ ULONG64\* arrayDimensionality) PURE; STDMETHOD(GetArrayDimensions)(\_In_ ULONG64 dimensions, \_Out_writes_(dimensions) ArrayDimension \*pDimensions) PURE;

[GetArrayDimensionality]()

The GetArrayDimensionality method returns the number of dimensions that the array is indexed in. For C style arrays, the value returned here will always be 1. 

[GetArrayDimensions]()

The GetArrayDimensions method returns a set of descriptors, one for each dimension of the array as indicated by the GetArrayDimensionality method. Each descriptor is an ArrayDimension structure which describes the starting index, length, and forward stride of each array dimension. This allows descriptions of significantly more powerful array constructs than are allowed in the C type system. 

For C-style arrays, a single array dimension is returned here with values which are always: 

- LowerBound = 0
- Length = ARRAYSIZE(array)
- Stride = sizeof(elementType)


**IDebugHostType2/IDebugHostType Function Related Methods**

Types which indicate that they are function types via a kind of TypeFunction support the following methods in both IDebugHostType and IDebugHostType2. 

```
//
// IDebugHostType:
//
STDMETHOD(GetFunctionCallingConvention)(_Out_ CallingConventionKind* conventionKind) PURE;
STDMETHOD(GetFunctionReturnType)(_COM_Outptr_ IDebugHostType** returnType) PURE;
STDMETHOD(GetFunctionParameterTypeCount)(_Out_ ULONG64* count) PURE;
STDMETHOD(GetFunctionParameterTypeAt)(_In_ ULONG64 i, _Out_ IDebugHostType** parameterType) PURE;
//
// IDebugHostType2:
//
STDMETHOD(GetFunctionVarArgsKind)(_Out_ VarArgsKind* varArgsKind) PURE;
```

[GetFunctionCallingConvention]()

The GetFunctionCallingConvention method returns the calling convention of the function. Such is returned as a member of the CallingConventionKind enumeration. 

[GetFunctionReturnType]()

The GetFunctionReturnType method returns the return type of the function. 

[GetFunctionParameterTypeCount]()

The GetFunctionParameterTypeCount method returns the number of arguments that the function takes. Note that the C/C++ ellipsis based variable argument marker is not considered in this count. The presence of such must be detected via the GetFunctionVarArgsKind method. This will only include arguments before the ellipsis. 

[GetFunctionParameterTypeAt]()

The GetFunctionParameterTypeAt method returns the type of the i-th argument to the function. 

The GetFunctionVarArgsKind method returns whether a given function utilizes a variable argument list, and if so, what style of variable arguments it utilizes. Such is defined by a member of the VarArgsKind enumeration defined as follows: 

 Enumerant | Meaning
|---------|---------|
VarArgsNone | The function does not take any variable arguments.
VarArgsCStyle | The function is a C-style varargs function (returnType(arg1, arg2, ...)). The number of arguments reported by the function does not include the ellipsis argument. Any variable argument passing occurs after the number of arguments returned by the GetFunctionParameterTypeCount method.


**IDebugHostType2 GetFunctionVarArgsKind**

The GetFunctionVarArgsKind method returns whether a given function utilizes a variable argument list, and if so, what style of variable arguments it utilizes. Such is defined by a member of the VarArgsKind enumeration defined as follows: 


**IDebugHostType2/IDebugHostType Typedef Related Methods**

Any type which is a typedef will behave as if the type is the final type underlying the typedef. This means that methods such as GetTypeKind will not indicate that the type is a typedef. Likewise, GetBaseType will not return the type the definition refers to. They will instead indicate behave as if they were called on the final definition underlying the typedef. As an example: 

```
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```

An IDebugHostType for 'either PMYSTRUCT or PTRMYSTRUCT will report the following information: 

- The GetTypeKind method will return TypePointer. The final underlying type MYSTRUCT * is indeed a pointer.
- The 'GetBaseType method will return a type for MYSTRUCT. The underlying type of MYSTRUCT * is MYSTRUCT.

The only difference here is how the typedef specific methods on IDebugHostType2 behave. Those methods are: 

```
STDMETHOD(IsTypedef)(_Out_ bool* isTypedef) PURE;
STDMETHOD(GetTypedefBaseType)(_Out_ IDebugHostType2** baseType) PURE;
STDMETHOD(GetTypedefFinalBaseType)(_Out_ IDebugHostType2** finalBaseType) PURE;
```

In this example: 

- The IsTypedef method will return true for both PMYSTRUCT and PTRMYSTRUCT
- The GetTypedefBaseType method will return MYSTRUCT * for PMYSTRUCT and PMYSTRUCT for PTRMYSTRUCT
- The GetTypedefFinalBaseType method will return MYSTRUCT * for both types

[IsTypedef]()

The IsTypedef method is the only method capable of seeing whether a type is a typedef. The GetTypeKind method will behave as if called on the underlying type. 

[GetTypedefBaseType]()

The GetTypedefBaseType method will return what the immediate definition of the typedef. In the examples described in the documentation: 

```
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```
this method will return MYSTRUCT * for PMYSTRUCT and PMYSTRUCT for PTRMYSTRUCT.


[GetTypedefFinalBaseType]()

The GetTypedefFinalBaseType method will return the final type that the typedef is a definition for. If the typedef is a definition of another typedef, this will continue to follow the definition chain until it reaches a type which is not a typedef and that type will be returned. In the examples described in the documentation: 

```
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```

this method will return MYSTRUCT * when called on either PMYSTRUCT or PTRMYSTRUCT. 

**IDebugHostType2/IDebugHostType Type Creation Methods**

```
STDMETHOD(CreatePointerTo)(_In_ PointerKind kind, _COM_Outptr_ IDebugHostType** newType) PURE;
STDMETHOD(CreateArrayOf)(_In_ ULONG64 dimensions, _In_reads_(dimensions) ArrayDimension *pDimensions, _COM_Outptr_ IDebugHostType** newType) PURE;
```

**Constant Symbol Values: IDebugHostConstant**

For locations where constant values are present in symbolic information (where a particular value is a symbol which may or may not be a constant value), the IDebugHostConstant interface expresses the notion of such a constant. This is typically used in places like template arguments where a given argument is typically a type but may instead be a non-type template argument (e.g.: a constant). 

The IDebugHostConstant interface is defined as follows (ignoring generic methods implemented by IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostConstant, IDebugHostSymbol)
{
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

[GetValue]()

The GetValue method returns the value of the constant packed into a VARIANT. It is important to note that the GetType method on IDebugHostSymbol may return a specific type symbol for the constant. In such cases, there is no guarantee that the packing of the constant value as defined by the type symbol is the same as the packing as returned by the GetValue method here. 


**Data Member Access: IDebugHostField**

The IDebugHostField class represents a symbol which is a data member of a class, structure, union, or other type construct. It does not represent free data (e.g.: global data). The interface is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostField, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetOffset)(_Out_ ULONG64* offset) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

[GetLocationKind]()

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. Such enumeration can be one of the following values: 

Enumerant | Meaning
|---------|--------|
LocationMember | The field is a regular data member of a class, structure, union, or other type construct. It has an offset which is relative to base address of the containing type construct. Such base address is typically represented by the this pointer. The offset of the field can be retrieved via the GetOffset method. The GetLocation and GetValue methods will fail for a field which is LocationMember.
LocationStatic | The field is static and has its own address. The GetLocation method will return the abstract location (e.g.: address) of the static field. The GetOffset and GetValue methods will fail for a field which is LocationStatic.
LocationConstant | The field is a constant and has a value. The GetValue method will return the value of the constant. The GetOffset and GetLocation methods will fail for a field which is LocationConstant
LocationNone | The field has no location. It may have been optimized out by the compiler or it may be a static field which is declared but never defined. Regardless of how such a field came to be, it has no physical presence or value. It is only in the symbols. All acquisition methods (GetOffset, GetLocation, and GetValue) will fail for a field which is LocationNone.

[GetOffset]()

For fields which have an offset (e.g.: fields whose location kind indicates LocationMember), the GetOffset method will return the offset from the base address of the containing type (the this pointer) to the data for the field itself. Such offsets are always expressed as unsigned 64-bit values. 
If the given field does not have a location which is an offset from the base address of the containing type, the GetOffset method will fail. 

[GetLocation]()

For fields which have an address regardless of the particular type instance (e.g.: fields whose location kind indicates LocationStatic), the GetLocation method will return the abstract location (address) of the field. 
If the given field does not have a static location, the GetLocation method will fail. 

[GetValue]()

For fields which have a constant value defined within the symbolic information (e.g.: fields whose location kind indicates LocationConstant), the GetValue method will return the constant value of the field. 
If the given field does not have a constant value, the GetValue method will fail. 


**Free Data Access: *IDebugHostData***

Data in modules which is not a member of another type is represented by the IDebugHostData interface. That interface is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostData, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

All of these methods are semantically equivalent to their counterparts in IDebugHostField. The only difference is that the GetLocationKind method will never return LocationMember for free data. 

[GetLocationKind]()

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. The description of this enumeration can be found in the documentation for IDebugHostField. 

[GetLocation]()

For data which has an address, the GetLocation method will return the abstract location (address) of the field. 
If the given data does not have a static location, the GetLocation method will fail. 

[GetValue]()

For datawhich has a constant value defined within the symbolic information (e.g.: data whose location kind indicates LocationConstant), the GetValue method will return the constant value of the field. 
If the given data does not have a constant value, the GetValue method will fail. 


**Base Classes: IDebugHostBaseClass**

The inheritance hierarchy of a given type is expressed through children of a type symbol. If a given type derives (inheritance wise) from one or more types, there will be one or more SymbolBaseClass children of the type symbol for the type. Each of those SymbolBaseClass symbols represent immediate inheritance from a particular type. The name of the base class is both the name of the SymbolBaseClass symbol as well as that of the type symbol for the base class. The GetType method on the SymbolBaseClass symbol can be used to get the type symbol for the base class itself. 
The full inheritance hierarchy can be traversed by recursively exploring SymbolBaseClass child symbols. 
Each of these base class symbols is expressed by the IDebugHostBaseClass interface which is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostBaseClass, IDebugHostSymbol)
{
    STDMETHOD(GetOffset)(_Out_ ULONG64* offset) PURE;
}
```

[GetOffset]()

The GetOffset method returns the offset of the base class from the base address of the derived class. Such offset may be zero or may be a positive unsigned 64-bit value. 


**Public Symbols: *IDebugHostPublic***

Public symbols represent things in the public table within a symbol file. They are, in effect, export addresses. There is no type information associated with a public symbol -- only an address. Unless a public symbol is explicitly requested by the caller, the debug host prefers to return private symbols for every inquiry. A public symbol is expressed by the IDebugHostPublic interface which is defined as follows (ignoring methods which are generic to IDebugHostSymbol): 

```
DECLARE_INTERFACE_(IDebugHostPublic, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
}
```

All of these methods are semantically equivalent to their counterparts in IDebugHostField. The only difference is that the GetLocationKind method will never return LocationMember or LocationConstant for such symbols. 

[GetLocationKind]()

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. The description of this enumeration can be found in the documentation for IDebugHostField. 

[GetLocation]()

For data which has an address, the GetLocation method will return the abstract location (address) of the field. 
If the given public does not have a static location, the GetLocation method will fail. 


**Module Signatures and Version Matching: *IDebugHostModuleSignature***

Module signatures represent a means to check whether a given module meets a set of criteria regarding naming and versioning. A module signature is created via the CreateModuleSignature method on IDebugHostSymbols. It can match the module name, and an optional range of version numbers for the module. Once such a signature is created, the client receives an IDebugHostModuleSignature interface which is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostModuleSignature, IUnknown)
{
    STDMETHOD(IsMatch)(_In_ IDebugHostModule* pModule, _Out_ bool* isMatch) PURE;
}
```

[IsMatch]()

The IsMatch method compares a particular module (as given by an IDebugHostModule symbol) against a signature, comparing the module name and version to the name and version range indicated in the signature. An indication of whether the given module symbol matches the signature is returned. 

**Type Signatures and Type Matching: *IDebugHostTypeSignature***

Type signatures represent a means to check whether a given type instance meets a set of criteria about the name of the type, the generic arguments to the type, and the module that the type is located within. A type signature is created via the CreateTypeSignature method on IDebugHostSymbols. Once such a signature is created, the client receives an IDebugHostTypeSignature interface which is defined as follows: 

```
DECLARE_INTERFACE_(IDebugHostTypeSignature, IUnknown)
{
    STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
    STDMETHOD(IsMatch)(_In_ IDebugHostType* type, _Out_ bool* isMatch, _COM_Outptr_opt_ IDebugHostSymbolEnumerator** wildcardMatches) PURE;
    STDMETHOD(CompareAgainst)(_In_ IDebugHostTypeSignature* typeSignature, _Out_ SignatureComparison* result) PURE;
}
```

[GetHashCode]()

The GetHashCode method returns a 32-bit hash code for the type signature. The debug host guarantees that there is synchronization in implementation between the hash code returned for type instances and the hash code returned for type signatures. With the exception of a global match, if a type instance is capable of matching a type signature, both will have the same 32-bit hash code. This allows an initial rapid comparison and match between a type instance and a plethora of type signatures registered with the data model manager. 

[IsMatch]()

The IsMatch method returns an indication of whether a particular type instance matches the criteria specified in the type signature. If it does, an indication of this is returned as well as an enumerator which will indicate all of the specific portions of the type instance (as symbols) which matched wildcards in the type signature. 

[CompareAgainst]()

The CompareAgainst method compares the type signature to another type signature and returns how the two signatures compare. The comparison result which is returned is a member of the SignatureComparison enumeration which is defined as follows: 

Enumerant | Meaning
|---------|-----------|
Unrelated | There is no relationship between the two signatures or types being compared.
Ambiguous |One signature or type compares ambiguously against the other. For two type signatures, this means that there are potential type instances which could match either signature equally well. As an example, the two type signatures shown below are ambiguous. Signature 1: *std::pair<*, int>* Signature 2: *std::pair<int, \*>* because the type instance std::pair<int, int> matches either one equally well (both have one concrete and one wildcard match).
LessSpecific | One signature or type is less specific than the other. Often, this means that the less specific signature has a wildcard where the more specific one has a concrete type. As an example, the first signature below is less specific than the second.Signature 1: *std::pair<*, int>* Signature 2: *std::pair<int, int>* because it has a wildcard (the *) where the second has a concrete type (int).
MoreSpecific | One signature or type is more specific than the other. Often, this means that the more specific signature has a concrete type where the less specific one has a wildcard. As an example, the first signature below is more specific than the second. Signature 1:  std::pair<int, int> Signature 2: std::pair<*, int> because it has a concrete type (int) where the second has a wildcard (the *).
Identical | The two signatures or types are identical.


## <span id="metadatainterfaces"></span> Debugger Data Model Metadata Interfaces

One of the core notions in the data model is that an object (particularly a synthetic one) is a dictionary of key/value/metadata tuples. Each key can have an entire store of metadata associated with it that describes a variety of things surrounding the key and its potential value. Note that the metadata does not, in any way, change the value of the key. It is only ancillary information associated with the key and its value which may affect the presentation or other associated attributes of the key and its value. 

In some senses, a metadata store is not all that different from the key/value/metadata tuples that are the essence of an object in the data model. It is, however, simplified from this view. A metadata store is represented by the IKeyStore interface. While also a collection of key/value/metadata tuples, there are limitations to what can be done with a metadata key store versus a model object: 

- A key store can only have a single parent store -- it cannot have an arbitrary chain of parent models.
- A key store has no concepts. It can only have the dictionary of key/value/metadata tuples. This means that the keys present in a key store are static. They can not be created on demand by a dynamic language system.
- By convention only, the values in a metadata defined key store are restricted to basic values (intrinsics and property accessors)

While a key store can have an arbitrary number (and arbitrary naming) of keys, there are certain names that have defined semantic values. Presently, those names are: 

Key Name | Value Type | Description
|--------------|------------------|--------------|
PreferredRadix | Integer: 2, 8, 10, or 16 | Indicates what radix an ordinal value should be displayed in
PreferredFormat | Integer: as defined by the PreferredFormat enumeration | Indicates the preferred formatting type for display of the value
PreferredLength | Integer | For arrays and other containers, indicates how many elements should be displayed by default
FindDerivation | Boolean | Indicates whether the debug host should perform derived type analysis on the value before using (e.g.: displaying)
Help | String | Tool tip style help text for the key which can be presented by the user interface in an appropriately helpful way.
ActionName | String | Indicates that the given method (one which takes no arguments and returns no values) is an action. The name of the action is specified in metadata. A user interface may utilize this name to present the option in a context menu or other appropriate interface
ActionIsDefault | Boolean | Only valid if the ActionName key is specified, indicates that this is the default action for the object.
ActionDescription | String | Only valid if the ActionName key is specified, this gives a tool tip style description for the action. Such text can be presented by the user interface in an appropriately helpful way.

Note that while keys in the metadata store can have their own metadata (ad infiniteum), there is currently no use for such. Most callers will specify null for any metadata parameters in methods on the IKeyStore interface. 

**The Core Metadata Interface: *IKeyStore***

The IKeyStore interface is defined as follows: 

```
DECLARE_INTERFACE_(IKeyStore, IUnknown)
{
   STDMETHOD(GetKey)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(SetKey)(_In_ PCWSTR key, _In_opt_ IModelObject* object, _In_opt_ IKeyStore* metadata) PURE;
   STDMETHOD(GetKeyValue)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(SetKeyValue)(_In_ PCWSTR key, _In_ IModelObject* object) PURE;
      STDMETHOD(ClearKeys)() PURE;
}
```

[GetKey]()

The GetKey method is analogous to the GetKey method on IModelObject. It will return the value of the specified key if it exists in the key store or the key store's parent store. Note that if the value of the key is a property accessor, the GetValue method will not be called on the property accessor. The actual IModelPropertyAccessor boxed into an IModelObject will be returned. It is typical that a client will call GetKeyValue for this reason. 

[SetKey]()

The SetKey method is analogous to the SetKey method on IModelObject. It is the only method which is capable of creating a key and associating metadata with it within the key store. 

[GetKeyValue]()

The GetKeyValue method is the first method a client will go to in order to find the value of a particular key within the metadata store. If the key specified by the key argument exists within the store (or it's parent store), the value of that key and any metadata associated with it will be returned. If the value of the key is a property accessor (an IModelPropertyAccessor boxed into an IModelObject), the GetValue method of the property accessor will automatically be called by GetKeyValue and the underlying value of the property returned. 

[SetKeyValue]()

The SetKeyValue method is analogous to the SetKeyValue method on IModelObject. This method is not capable of creating a new key within the metadata store. If there is an existing key as indicated by the key argument, its value will be set as indicated. If the key is a property accessor, the SetValue method will be called on the property accessor in order to set the underlying value. Note that metadata is typically static once created. Use of this method on a metadata key store should be infrequent. 

[ClearKeys]()

The ClearKeys method is analogous to the ClearKeys method on IModelObject. It will remove every key from the given metadata store. This method has no effect on any parent store. 




## <span id="related_topics"></span>Related topics

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

 

 






