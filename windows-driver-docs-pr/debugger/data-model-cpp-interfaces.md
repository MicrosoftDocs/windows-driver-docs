---
title: Debugger Data Model C++ Interfaces
description: This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.author: domars
ms.date: 03/30/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Data Model C++ Interfaces

This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

This page is part of a series on which describes the interfaces accessible from C++, how to use them to build a C++ based
debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.


Theses section in this topic introduce the the following.

[Overview of Debugger Debugger Data Model C++ Interfaces](#overview)

[Summary of Debugger Data Model Interfaces](#summary)

[The Core Object Model](#core)

[The Core Object Model - IModelObject](#imodelobject)

[Data Model C++ Host Interfaces](#interface)


[Object Enumeration in the Data Model](#object)


[The Core Object Model - IModelObject](#imodelobject)

[The Core Object Model - IModelObject](#imodelobject)




## <span id="Overview"> Overview of Debugger Debugger Data Model C++ Interfaces

The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's newer (dx) expression evaluator as well as from JavaScript extensions or other C++ extensions for that matter. 




## <span id="summary"> Summary of Debugger Data Model Interfaces

There are a multitude of C++ interfaces which comprise different pieces of the data model. In order to approach these interfaces in a consistent and easy manner, they are broken down by general category. The main areas here: 

**The General Object Model**

The first and most important set of interfaces define how to get access to the core data model and how to access and manipulate objects. IModelObject is the interface which represents every object in the data model (much like C#'s object). This is the main interface of interest for both consumers of and producers to the data model. The other interfaces are mechanisms for accessing different aspects of objects. 
The following interfaces are defined for this category: 


*Bridges Between DbgEng and the Data Model*
IHostDataModelAccess

*Main Interfaces* 

IModelObject

IKeyStore

IModelIterator

IModelPropertyAccessor

IModelMethod

IKeyEnumerator

IRawEnumerator

IModelKeyReference / IModelKeyReference2

*Concept Interfaces*

IStringDisplayableConcept

IIterableConcept

IIndexableConcept

IPreferredRuntimeTypeConcept

IDataModelConcept

IDynamicKeyProviderConcept

IDynamicConceptProviderConcept


**Management of Data Models and Extensibility**

The Data Model Manager is the core component which manages how all extensibility occurs. It is the central repository of a set of tables which map both native types to extension points as well as synthetic constructs to extension points. In addition, it is the entity which is responsible for the boxing of objects (conversion of ordinal values or strings into IModelObject's). 

The following interfaces are defined for this category: 

*General Data Model Manager Access* 

IDataModelManager / IDataModelManager2

Script Management 

IDataModelScriptManager

IDataModelScriptProviderEnumerator

**Access to the Debugger's Type System and Memory Spaces**

The underlying type system and memory spaces of the debugger are exposed in detail for extensions to make use of. 
The following interfaces are defined for this category: 

*General Host (Debugger) Interfaces*

IDebugHost

IDebugHostStatus

IDebugHostContext

IDebugHostMemory / IDebugHostMemory2

IDebugHostErrorSink

IDebugHostEvaluator / IDebugHostEvaluator2

IDebugHostExtensibility

Host (Debugger) Type System Interfaces 

IDebugHostSymbols

IDebugHostSymbol / IDebugHostSymbol2

IDebugHostModule

IDebugHostType / IDebugHostType2

IDebugHostConstant

IDebugHostField

IDebugHostData

IDebugHostBaseClass

IDebugHostPublic

IDebugHostModuleSignature

IDebugHostTypeSignature


*Host (Debugger) Support for Scripting* 

IDebugHostScriptHost

**Authoring and Consuming Scripts**

The Data Model also has a general notion of what a script is and how to debug one. It is entirely possible for a debugger extension to come along and define a general bridge between the data model and another dynamic language (usually a scripting environment). This set of interfaces is how that is accomplished as well as how a debugger UI can make use of such scripts. 

The following interfaces are defined for this category: 

*General Script Interfaces* 


IDataModelScriptProvider

IDataModelScript

IDataModelScriptClient

IDataModelScriptHostContext

IDataModelScriptTemplate

IDataModelScriptTemplateEnumerator

IDataModelNameBinder

*Script Debugger Interfaces* 

IDataModelScriptDebug

IDataModelScriptDebugClient

IDataModelScriptDebugStack

IDataModelScriptDebugStackFrame

IDataModelScriptDebugVariableSetEnumerator

IDataModelScriptDebugBreakpoint

IDataModelScriptDebugBreakpointEnumerator


## <span id="core">  The Core Object Model

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

An *IModelObject* is not an object in isolation. In addition to
representing one of the types of objects shown above, each object has
the notion of a chain of parent data models. This chain behaves much
like a [| JavaScript prototype
chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain).
Instead of a linear chain of prototypes like JavaScript has, each data
model object defines a linear chain of **parent models**. Each of those
parent models in turn has another linear chain of its own set of
parents. In essence, each object is an aggregation of the capabilities
(properties, etc...) of both itself and every object in this tree. When
a specific property is queried, if the object it is queried on does not
support that property, the query is passed in linear order to each
parent in turn. This creates a behavior where the search for a property
is resolved by a depth-first search of the aggregate tree.

Extensibility within this object model is very simple given this notion
that every object is an aggregate of itself and the tree of parent
models. An extension can come in and add itself into the list of parent
models for another object. Doing this **extends** the object. In this
manner, it is possible to add capabilities onto anything: a particular
instance of an object or value, a native type, the debugger's concept of
what a process or thread is, or even the notion of "all iterable
objects".

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






## <span id="imodelobject"></span> The Core Object Interface: **IModelObject**

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



## <span id="interface"></span> Data Model C++ Host Interfaces

**The Data Model Host**

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


## <span id="object"></span> Foo


## <span id="object"></span> Foo


## <span id="object"></span> Foo


## <span id="object"></span> Foo


## <span id="related_topics"></span>Related topics


[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

 

 






