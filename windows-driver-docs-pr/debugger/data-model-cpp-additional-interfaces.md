---
title: Debugger Data Model C++ Additional Interfaces
description: This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.author: domars
ms.date: 04/11/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Data Model C++ Interfaces

This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

This page is part of a series on which describes the interfaces accessible from C++, how to use them to build a C++ based
debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.

[Debugger Data Model C++ Interfaces Overview](data-model-cpp-interfaces-overview.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)


## Topic Orginization

These sections in this topic introduce the the following.

- [Debugger Data Model Metadata Interfaces](#metadatainterfaces)

- [Object Enumeration in the Data Model](#object)

- [Concepts in the Data Model](#concepts) 



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




## <span id="concepts"> Concepts in the Data Model 

Synthetic objects in the data model are effectively two things: 

- A dictionary of key/value/metadata tuples.
- A set of concepts (interfaces) that are supported by the data model.
Concepts are interfaces that a client (as opposed to the data model) implements to provide a specified set of semantic behavior. The currently supported set of concepts are listed here. 

Concept Interface | Description
|-----------------|-------------|
IDataModelConcept | The concept is a parent model. If this model is automatically attached to a native type via a registered type signature, the InitializeObject method will automatically be called every time a new object of such type is instantiated.
IStringDisplayableConcept | The object can be converted to a string for display purposes.
IIterableConcept | The object is a container and can be iterated.
IIndexableConcept | The object is a container and can be indexed (accessed via random access) in one or more dimensions.
IPreferredRuntimeTypeConcept | The object understands more about types derived from it than the underlying type system is capable of providing and would like to handle its own conversions from static to runtime type.
IDynamicKeyProviderConcept | The object is a dynamic provider of keys and wishes to take over all key queries from the core data model. This interface is typically used as a bridge to dynamic languages such as JavaScript.
IDynamicConceptProviderConcept | The object is a dynamic provider of concepts and wishes to take over all concept queries from the core data model. This interface is typically used as a bridge to dynamic languages such as JavaScript.


**The Data Model Concept: IDataModelConcept**

Any model object which is attached to another model object as a parent model must directly support the data model concept. The data model concept requires support of an interface, IDataModelConcept defined as follows. 

```
DECLARE_INTERFACE_(IDataModelConcept, IUnknown)
{
    STDMETHOD(InitializeObject)(_In_ IModelObject* modelObject, _In_opt_ IDebugHostTypeSignature* matchingTypeSignature, _In_opt_ IDebugHostSymbolEnumerator* wildcardMatches) PURE;
    STDMETHOD(GetName)(_Out_ BSTR* modelName) PURE;
}
```

[InitializeObject]()

A data model can be registered as the canonical visualizer or as an extension for a given native type through the data model manager's RegisterModelForTypeSignature or RegisterExtensionForTypeSignature methods. When a model is registered via either of these methods, the data model is automatically attached as a parent model to any native object whose type matches the signature passed in the registration. At the point where that attachment is automatically made, the InitializeObject method is called on the data model. It is passed the instance object, the type signature which caused the attachment, and an enumerator which produces the type instances (in linear order) which matched any wildcards in the type signature. The data model implementation may use this method call to initialize any caches it requires. 

[GetName]()

If a given data model is registered under a default name via the RegisterNamedModel method, the registered data model's IDataModelConcept interface must return that name from this method. Note that it is perfectly legitimate for a model to be registered under multiple names (the default or best one should be returned here). A model may be completely unnamed (so long as it is not registered under a name). In such circumstances, the GetName method should return E_NOTIMPL. 


**The String Displayable Concept: IStringDisplayableConcept**

An object which wishes to provide a string conversion for display purposes can implement the string displayable concept through implementation of the IStringDisplayableConcept interface. The interface is defined as follows: 

```
DECLARE_INTERFACE_(IStringDisplayableConcept, IUnknown)
{
    STDMETHOD(ToDisplayString)(_In_ IModelObject* contextObject, _In_opt_ IKeyStore* metadata, _Out_ BSTR* displayString) PURE;
}
```

[ToDisplayString]()

The ToDisplayString method is called whenever a client wishes to convert an object into a string to display (to console, in the UI, etc...). Such a string conversion should not be used for the basis of additional programmatic manipulation. The string conversion itself may be deeply influenced by the metadata passed to the call. A string conversion should make every attempt to honor the PreferredRadix and PreferredFormat keys. 


**The Iterable Concept: IIterableConcept and IModelIterator**

An object which is a container of other objects and wishes to express the ability to iterate over those contained objects can support the iterable concept by an implementation of the IIterableConcept and IModelIterator interfaces. There is a very important relationship between support of the iterable concept and support of the indexable concept. An object which supports random access to the contained objects can support the indexable concept in addition to the iterable concept. In this case, the iterated elements must also produce a default index which, when passed to the indexable concept refer to the same object. A failure to satisfy this invariant will result in undefined behavior in the debug host. 

The IIterableConcept is defined as follows: 

```
DECLARE_INTERFACE_(IIterableConcept, IUnknown)
{
    STDMETHOD(GetDefaultIndexDimensionality)(_In_ IModelObject* contextObject, _Out_ ULONG64* dimensionality) PURE;
    STDMETHOD(GetIterator)(_In_ IModelObject* contextObject, _Out_ IModelIterator** iterator) PURE;
}
```

The IModelIterator Concept is defined as follows: 

```
DECLARE_INTERFACE_(IModelIterator, IUnknown)
{
   STDMETHOD(Reset)() PURE;
   STDMETHOD(GetNext)(_COM_Errorptr_ IModelObject** object, _In_ ULONG64 dimensions, _Out_writes_opt_(dimensions) IModelObject** indexers, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
}
```

IIterableConcept's [GetDefaultIndexDimensionality]()

The GetDefaultIndexDimensionality method returns the number of dimensions to the default index. If an object is not indexable, this method should return 0 and succeed (S_OK). Any object which returns a non-zero value from this method is declaring support for a protocol contract which states: 
- The object supports the indexable concept via support of IIndexableConcept
- The GetNext method of the IModelIterator returned from the GetIterator method of the iterable concept will return a unique default index for each produced element. Such index will have the number of dimensions as indicated here.
- Passing the indicies returned from the GetNext method of the IModelIterator to the GetAt method on the indexable concept (IIndexableConcept) will refer to the same object that GetNext produced. The same value is returned.

IIterableConcept's [GetIterator]()

The GetIterator method on the iterable concept returns an iterator interface which can be used to iterate the object. The returned iterator must remember the context object that was passed to the GetIterator method. It will not be passed to methods on the iterator itself. 


IModelIterator's [Reset]()

The Reset method on an iterator returned from the iterable concept will restore the position of the iterator to where it was when the iterator was first created (before the first element). While it is strongly recommended that iterator's support the Reset method, it is not required. An iterator can be the equivalent of a C++ input iterator and only allow a single pass of forward iteration. In such case, the Reset method may fail with E_NOTIMPL. 

IModelIterator's [GetNext]()

The GetNext method moves the iterator forward and fetches the next iterated element. If the object is indexable in addition to being iterable and this is indicated by the GetDefaultIndexDimensionality argument returning a non-zero value, this method may optionally return the default indicies to get back to the produced value from the indexer. Note that a caller may choose to pass 0/nullptr and not retrieve any indicies. It is considered illegal for the caller to request partial indicies (e.g.: less than the number produced by GetDefaultIndexDimensionality). 

If the iterator moved forward successfully but there was an error in reading the value of the iterated element, the method may return an error *AND* fill "object" with an error object. 
At the end of iteration of the contained elements, the iterator will return E_BOUNDS from the GetNext method. Any subsequent call (unless there has been an intervening Reset call) will also return E_BOUNDS. 


**The Indexable Concept: IIndexableConcept**

An object which wishes to provide random access to a set of contents can support the indexable concept via support of the IIndexableConcept interface. Most objects which are indexable will be iterable as well through support of the iterable concept. This is not, however, required. If supported, there is an important relationship between the iterator and indexer. The iterator must support the GetDefaultIndexDimensionality, return a non-zero value from that method, and support the contract documented there. 
The indexer concept interface is defined as follows: 

```
DECLARE_INTERFACE_(IIndexableConcept, IUnknown)
{
    STDMETHOD(GetDimensionality)(_In_ IModelObject* contextObject, _Out_ ULONG64* dimensionality) PURE;
    STDMETHOD(GetAt)(_In_ IModelObject* contextObject, _In_ ULONG64 indexerCount, _In_reads_(indexerCount) IModelObject** indexers, _COM_Errorptr_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    STDMETHOD(SetAt)(_In_ IModelObject* contextObject, _In_ ULONG64 indexerCount, _In_reads_(indexerCount) IModelObject** indexers, _In_ IModelObject *value) PURE;
}
```

An example of using the indexer (and its interplay with the iterator) is shown below. This example iterates the contents of an indexable container and uses the indexer to get back to the value which was just returned. While that operation is functionally useless as written, it demonstrates how these interfaces interact. Note that the example below does not deal with memory allocation failure. It assumes a throwing new (which might be a poor assumption depending on the environment in which the code exists -- the COM methods of the data model cannot have C++ exceptions escape): 

```
ComPtr<IModelObject> spObject;

//
// Assume we have gotten some object in spObject that is iterable (e.g.: an object which represents a std::vector<SOMESTRUCT>)
//
ComPtr<IIterableConcept> spIterable;
ComPtr<IIndexableConcept> spIndexer;
if (SUCCEEDED(spObject->GetConcept(__uuidof(IIterableConcept), &spIterable, nullptr)) &&
    SUCCEEDED(spObject->GetConcept(__uuidof(IIndexableConcept), &spIndexable, nullptr)))
{
    ComPtr<IModelIterator> spIterator;

    //
    // Determine how many dimensions the default indexer is and allocate the requisite buffer.
    //
    ULONG64 dimensions;
    if (SUCCEEDED(spIterable->GetDefaultIndexDimensionality(spObject.Get(), &dimensions)) && dimensions > 0 &&
        SUCCEEDED(spIterable->GetIterator(spObject.Get(), &spIterator)))
    {
        std::unique_ptr<ComPtr<IModelObject>[]> spIndexers(new ComPtr<IModelObject>[dimensions]);

        //
        // We have an iterator.  Error codes have semantic meaning here.  E_BOUNDS indicates the end of iteration.  E_ABORT indicates that
        // the debugger host or application is trying to abort whatever operation is occurring.  Anything else indicates
        // some other error (e.g.: memory read failure) where the iterator MIGHT still produce values.
        //
        for(;;)
        {
            ComPtr<IModelObject> spContainedStruct;
            ComPtr<IKeyStore> spContainedMetadata;

            //
            // When we fetch the value from the iterator, it will pass back the default indicies.
            //
            HRESULT hr = spIterable->GetNext(&spContainedStruct, dimensions, reinterpret_cast<IModelObject **>(spIndexers.get()), &spContainedMetadata);
            if (hr == E_BOUNDS || hr == E_ABORT)
            {
                break;
            }

            if (FAILED(hr))
            {
                //
                // Decide how to deal with failure to fetch an element.  Note that spContainedStruct *MAY* contain an error object
                // which has detailed information about why the failure occurred (e.g.: failure to read memory at address X).
                //
            }

            //
            // Use the indexer to get back to the same value.  We already have them, so there isn't much functional point to this.  It simply
            // highlights the interplay between iterator and indexer.
            //
            ComPtr<IModelObject> spIndexedStruct;
            ComPtr<IKeyStore> spIndexedMetadata;

            if (SUCCEEDED(spIndexer->GetAt(spObject.Get(), dimensions, reinterpret_cast<IModelObject **>(spIndexers.get()), &spIndexedStruct, &spIndexedMetadata)))
            {
                //
                // spContainedStruct and spIndexedStruct refer to the same object.  They may not have interface equality.
                // spContainedMetadata and spIndexedMetadata refer to the same metadata store with the same contents.  They may not have interface equality.
                //
            }
        }
    }
}
```


[GetDimensionality]()

The GetDimensionality method returns the number of dimensions that the object is indexed in. Note that if the object is both iterable and indexable, the implementation of GetDefaultIndexDimensionality must agree with the implementation of GetDimensionality as to how many dimensions the indexer has. 

[GetAt]()

The GetAt method retrieves the value at a particular N-dimensional index from within the indexed object. An indexer of N-dimensions where N is the value returned from GetDimensionality must be supported. Note that an object may be indexable in different domains by different types (e.g.: indexable via both ordinals and strings). If the index is out of range (or could not be accessed), the method will return a failure; however, in such cases, the output object may still be set to an error object. 

[SetAt]()

The SetAt method attempts to set the value at a particular N-dimensional index from within the indexed object. An indexer of N-dimensions where N is the value returned from GetDimensionality must be supported. Note that an object may be indexable in different domains by different types (e.g.: indexable via both ordinals and strings). Some indexers are read-only. In such cases, E_NOTIMPL will be returned from any call to the SetAt method. 


**The Preferred Runtime Type Concept: IPreferredRuntimeTypeConcept**

A debug host can be queried to make an attempt to determine the real runtime type of an object from a static type found in symbolic information. This conversion may be based on completely accurate information (e.g.: C++ RTTI) or may be based on strong heuristics such as the shape of any virtual function tables within the object. Some objects, however, cannot be converted from a static to a runtime type because they do not fit into the heuristics of the debug host (e.g.: they have no RTTI or virtual function tables). In such cases, a data model for an object can choose to override the default behavior and declare that it knows more about the "runtime type" of an object than the debug host is capable of understanding. This is done through the preferred runtime type concept and support of the IPreferredRuntimeTypeConcept interface. 

The IPreferredRuntimeTypeConcept interface is declared as follows: 

```
DECLARE_INTERFACE_(IPreferredRuntimeTypeConcept, IUnknown)
{
    STDMETHOD(CastToPreferredRuntimeType)(_In_ IModelObject* contextObject, _COM_Errorptr_ IModelObject** object) PURE;
}
```

[CastToPreferredRuntimeType]()

The CastToPreferredRuntimeType method is called whenever a client wishes to attempt to convert from a static type instance to the runtime type of that instance. If the object in question supports (through one of its attached parent models) the preferred runtime type concept, this method will be called to perform the conversion. This method may either return the original object (there is no conversion or it could not be analyzed), return a new instance of the runtime type, fail for non-semantic reasons (e.g.: out of memory), or return E_NOT_SET. The E_NOT_SET error code is a very special error code which indicates to the data model that the implementation does not want to override the default behavior and that the data model should fall back to whatever analysis is performed by the debug host (e.g.: RTTI analysis, examination of the shape of the virtual function tables, etc...) 


**The Dynamic Provider Concepts: IDynamicKeyProviderConcept and IDynamicConceptProviderConcept**

While the data model itself normally handles key and concept management for objects, there are times where that notion is less than ideal. In particular, when a client wishes to create a bridge between the data model and something else which is truly dynamic (e.g.: JavaScript), it can be valuable to take over key and concept management from the implementation in the data model. As the core data model is the one and only implementation of IModelObject, this is instead done via a combination of two concepts: the dynamic key provider concept and the dynamic concept provider concept. While it would be typical to implement both or neither, there is no requirement for such. 

If both are implemented, the dynamic key provider concept must be added before the dynamic concept provider concept. 
Both of these concepts are special. They effectively flip a switch on the object changing it from "statically managed" to "dynamically managed". These concepts can only be set if there are no keys/concepts managed by the data model on the object. Once these concepts are added to an object, the action of doing this is irrevocable. 

There is an additional semantic difference around extensibility between an IModelObject which is a dynamic concept provider and one that is not. These concepts are intended to allow clients to create bridges between the data model and dynamic language systems such as JavaScript. The data model has a concept of extensibility that differs somewhat fundamentally from systems like JavaScript in that there is a tree of parent models rather than a linear chain like the JavaScript prototype chain. To allow a better relationship to such systems, an IModelObject which is a dynamic concept provider has a single data model parent. That single data model parent is a normal IModelObject which can have an arbitrary number of parent models as is typical for the data model. Any requests to the dynamic concept provider to add or remove parents are automatically redirected to the single parent. From an outsider's perspective, it looks as though the dynamic concept provider has a normal tree style chain of parent models. The implementer of the dynamic concept provider concept is the only object (outside of the core data model) that is aware of the intermediate single parent. That single parent can be linked against the dynamic language system to provide a bridge (e.g.: placed into the JavaScript prototype chain). 

The dynamic key provider concept is defined as follows: 

```
DECLARE_INTERFACE_(IDynamicKeyProviderConcept, IUnknown)
{
    STDMETHOD(GetKey)(_In_ IModelObject *contextObject, _In_ PCWSTR key, _COM_Outptr_opt_result_maybenull_ IModelObject** keyValue, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata, _Out_opt_ bool *hasKey) PURE;
    STDMETHOD(SetKey)(_In_ IModelObject *contextObject, _In_ PCWSTR key, _In_ IModelObject *keyValue, _In_ IKeyStore *metadata) PURE;
    STDMETHOD(EnumerateKeys)(_In_ IModelObject *contextObject, _COM_Outptr_ IKeyEnumerator **ppEnumerator) PURE;
}
```

The dynamic concept provider concept is defined as follows: 

```
DECLARE_INTERFACE_(IDynamicConceptProviderConcept, IUnknown)
{
    STDMETHOD(GetConcept)(_In_ IModelObject *contextObject, _In_ REFIID conceptId, _COM_Outptr_result_maybenull_ IUnknown **conceptInterface, _COM_Outptr_opt_result_maybenull_ IKeyStore **conceptMetadata, _Out_ bool *hasConcept) PURE;
    STDMETHOD(SetConcept)(_In_ IModelObject *contextObject, _In_ REFIID conceptId, _In_ IUnknown *conceptInterface, _In_opt_ IKeyStore *conceptMetadata) PURE;
    STDMETHOD(NotifyParent)(_In_ IModelObject *parentModel) PURE;
    STDMETHOD(NotifyParentChange)(_In_ IModelObject *parentModel) PURE;
    STDMETHOD(NotifyDestruct)() PURE;
}
```

IDynamicKeyProviderConcept's [GetKey]()

The GetKey method on a dynamic key provider is largely an override of the GetKey method on IModelObject. The dynamic key provider is expected to return the value of the key and any metadata associated with that key. In the event that the key is not present (but no other error occurs), the provider must return false in the hasKey parameter and succeed with S_OK. Failing this call is considered a failure to fetch a key and will explicitly halt the search for the key through the parent model chain. Returning false in hasKey and success will continue the search for the key. 
Note that it is perfectly legal for GetKey to return a boxed property accessor as the key. This would be semantically identical to the GetKey method on IModelObject returning a property accessor. 

IDynamicKeyProviderConcept's [SetKey]()

The SetKey method on a dynamic key provider is effectively an override of the SetKey method on IModelObject. This sets a key in the dynamic provider. It is effectively the creation of a new property on the provider. Note that a provider which does not support any notion of something like the creation of expando properties should return E_NOTIMPL here. 

IDynamicKeyProviderConcept's [EnumerateKeys]()

The EnumerateKeys method on a dynamic key provider is effectively an override of the EnumerateKeys method on IModelObject. This enumerates all the keys in the dynamic provider. The returned enumerator has several restrictions that must be honored by the implementation: 

- It must behave as a call to EnumerateKeys and not EnumerateKeyValues or EnumerateKeyReferences. It must return the key values not resolving any underlying property accessors (if such concept exists in the provider).
- From the perspective of a single dynamic key provider, it is illegal to enumerate multiple keys of the same name that are physically distinct keys. This can happen on different providers that are attached through the parent model chain, but it cannot happen from the perspective of a single provider.

IDynamicConceptProvider's [GetConcept]()

The GetConcept method on a dynamic concept provider is effectively an override of the GetConcept method on IModelObject. The dynamic concept provider must return an interface for the queried concept if it exists as well as any metadata associated with that concept. If the concept does not exist on the provider, that must be indicated via a false value being returned in the hasConcept argument and a successful return. Failure of this method is a failure to fetch the concept and will explicitly halt the search for the concept. Returning false for hasConcept and a successful code will continue the search for the concept through the parent model tree. 

IDynamicConceptProvider's [SetConcept]()

The SetConcept method on a dynamic concept provider is effectively an override of the SetConcept method on IModelObject. The dynamic provider will assign the concept. This may make the object iterable, indexable, string convertible, etc... Note that a provider which does not allow the creation of concepts on it should return E_NOPTIMPL here. 

IDynamicConceptProvider's [NotifyParent]()

The NotifyParent call on a dynamic concept provider is used by the core data model to inform the dynamic provider of the single parent model which is created to allow for bridging the "multiple parent models" paradigm of the data model to more dynamic languages. Any manipulation of that single parent model will cause further notifications to the dynamic provider. Note that this callback is made immediately upon assignment of the dynamic concept provider concept. 

IDynamicConceptProvider's [NotifyParentChange]()

The NotifyParent method on a dynamic concept provider is a callback made by the core data model when a static manipulation of the object's single parent model is made. For any given parent model added, this method will be called a first time when said parent model is added and a second time if/when said parent model is removed. 

IDynamicConceptProvider's [NotifyDestruct]()

The NotifyDestruct method on a dynamic concept provider is a callback made by the core data model at the start of destruction of the object which is a dynamic concept provider. It provides additional clean up opportunities to clients which require it. 


---

## <span id="related_topics"></span>Related topics

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

 

 






