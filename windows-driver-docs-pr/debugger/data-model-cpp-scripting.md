---
title: Debugger Data Model C++ Scripting
description: This topic describes how to use Debugger Data Model C++ scripting to support automation with the debugger engine.
ms.date: 09/12/2019
---

# Debugger Data Model C++ Scripting

This topic describes how to use Debugger Data Model C++ Debugger Data Model C++ scripting to support automation with the debugger engine using scripting.

## <span id="scriptmanangement"> Script Management in the Debugger Data Model 

In addition to the Data Model Manager's role as the central authority on object creation and extensibility, it is also responsible for the management of an abstract concept of scripts. From the perspective of the Script Manager portion of the Data Model Manager, a script is something which can be dynamically loaded, unloaded, and potentially debugged by a provider in order to extend or provide new functionality to the data model. 

A script provider is a component which bridges a language (e.g.: NatVis, JavaScript, etc...) to the data model. It registers one or more file extensions (e.g.: ".NatVis", ".js") which are handled by the provider allowing a debugger client or a user interface to allow for loading of script files with that particular extension by delegation to the provider. 

**The Core Script Manager: IDataModelScriptManager**

The core script manager interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptManager, IUnknown)
{
    STDMETHOD(GetDefaultNameBinder)(_COM_Outptr_ IDataModelNameBinder **ppNameBinder) PURE;
    STDMETHOD(RegisterScriptProvider)(_In_ IDataModelScriptProvider *provider) PURE;
    STDMETHOD(UnregisterScriptProvider)(_In_ IDataModelScriptProvider *provider) PURE;
    STDMETHOD(FindProviderForScriptType)(_In_ PCWSTR scriptType, _COM_Outptr_ IDataModelScriptProvider **provider) PURE;
    STDMETHOD(FindProviderForScriptExtension)(_In_ PCWSTR scriptExtension, _COM_Outptr_ IDataModelScriptProvider **provider) PURE;
    STDMETHOD(EnumerateScriptProviders)(_COM_Outptr_ IDataModelScriptProviderEnumerator **enumerator) PURE;
}
```

[GetDefaultNameBinder](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptmanager-getdefaultnamebinder)

The GetDefaultNameBinder method returns the data model's default script name binder. A name binder is a component which resolves a name within the context of an object. For instance, given the expression "foo.bar", a name binder is called upon to resolve the name bar in the context of object foo. The binder returned here follows a set of default rules for the data model. Script providers can use this binder to provide consistency in name resolution across providers. 


[RegisterScriptProvider](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptmanager-registerscriptprovider)

The RegisterScriptProvider method informs the data model that a new script provider exists which is capable of bridging a new language to the data model. When this method is called, the script manager will immediately call back the given script provider and inquire about the properties of the scripts it manages. If there is already a provider registered under the name or file extension which the given script provider indicates, this method will fail. Only a single script provider can be registered as the handler for a particular name or file extension. 


[UnregisterScriptProvider](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptmanager-unregisterscriptprovider)

The UnregisterScriptProvider method undoes a call to the RegisterScriptProvider method. The name and file extension given by the inpassed script provider will no longer be associated with it. It is important to note that there may be a significant number of outstanding COM references to the script provider even after unregistration. This method only prevents the loading/creation of scripts of the type that the given script provider manages. If a script loaded by that provider is still loaded or has manipulated the object model of the debugger (or data model), those manipulations may still have references back into the script. There may be data models, methods, or objects which directly reference constructs in the script. A script provider must be prepared to deal with that. 


[FindProviderForScriptType](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptmanager-findproviderforscripttype)

The FindProviderForScriptType method searches the script manager for a provider which has a script type string as indicated in this method. If one cannot be found, this method will fail; otherwise, such script provider will be returned to the caller. 


[EnumerateScriptProviders](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptmanager-enumeratescriptproviders)

The EnumerateScriptProviders method will return an enumerator which will enumerate every script provider that has been registered with the script manager via a prior call to the RegisterScriptProvider method. 



**Script Provider Enumeration: IDataModelScriptProviderEnumerator**

The EnumerateScriptProviders method will return an enumerator of the following form:

```cpp 
DECLARE_INTERFACE_(IDataModelScriptProviderEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_COM_Outptr_ IDataModelScriptProvider **provider) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptproviderenumerator-reset)

The Reset method will move the enumerator to the position it was at prior to returning the first element. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptproviderenumerator-getnext)

The GetNext method will move the enumerator forward one element and return the script provider which is at that element. When the enumerator hits the end of enumeration, E_BOUNDS will be returned. Calling the GetNext method after receiving this error will continue to return E_BOUNDS indefinitely. 



## <span id="hostinterfacesscript"> Debugger Data Model C++ Host Interfaces for Scripting

**The Host's Role in Scripting**

The debug host exposes a series of very low level interfaces for understanding the nature of the type system of its debug target(s), evaluating expressions in the language of its debug target(s), etc... Normally, it is unconcerned with higher level constructs like scripting. Such is left to the overall debugger application or to extensions which provide these capabilities. There is, however, an exception to this. Any debug host which wants to participate in the overall scripting experience afforded by the data model needs to implement a few simple interfaces to provide contexts to scripts. In effect, the debug host is in control of where it wants the scripting environment to place functions and other script provided functionality within the namespace of the data model. Being involved in this process allows the host to allow (or not) the use of such functions in, for instance, its expression evaluator. 
The interfaces involved from the host's perspective here are: 

Interface | Description
|---------|------------|
IDebugHostScriptHost | The interface which indicates the capability of the debug host to take part in the scripting environment. This interface allows for the creation of contexts which inform scripting engines of where to place objects.
IDataModelScriptHostContext | A host interface which is used by the script provider as a container for the contents of the script. How the contents of a script surface other than the manipulations that it performs to the object model of the debugger application is up to the particular debug host. This interface allows the script provider to get information about where to place its contents. See [Data Model C++ Scripting Interfaces](#scriptinterface) later in this topic for more information.


**The Debug Host's Script Host: IDebugHostScriptHost**

The IDebugHostScriptHost interface is the interface used by a script provider to get a context from the debug host for a newly created script. This context includes an object (provided by the debug host) where the script provider can place any bridges between the data model and the scripting environment. Such bridges might, for instance, be data model methods which invoke script functions. Doing this allows a caller on the data model side to invoke script methods by utilization of the Call method on IModelMethod interface. 

The IDebugHostScriptHost interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDebugHostScriptHost, IUnknown)
{
    STDMETHOD(CreateContext)(_In_ IDataModelScript* script, _COM_Outptr_ IDataModelScriptHostContext** scriptContext) PURE;
}
```

[CreateContext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idebughostscripthost-createcontext)

The CreateContext method is called by a script provider to create a new context in which to place the contents of the script. Such context is represented by the IDataModelScriptHostContext interface described in detail on the Data Model C++ Scripting Interfaces page. 


## <span id="scriptinterface"> Debugger Data Model C++ Scripting Interfaces

**Scripting and Script Interfaces**

The overall architecture of the data model allows a third party to define a bridge between some language and the object model of the data model. Typically, the language being bridged is a scripting language since the environment of the data model is very dynamic. A component which defines and implements this bridge between a language and the object model of the data model is called a script provider. When initialized, a script provider registers itself with the script manager portion of the data model manager and any interface which manages extensibility will subsequently allow for the editing, loading, unloading, and potentially debugging of scripts written to the language that the script provider manages. 

Note that Debugging Tools for Windows presently defines two script providers.

- The NatVis Provider. This provider is embedded within DbgEng.dll and bridges between NatVis XML and data models, allowing visualization of native/language data types.
- The JavaScript Provider. This provider is contained within a legacy debugger extension: JsProvider.dll. It bridges between scripts written in the JavaScript language and the data model, allowing for arbitrary forms of debugger control and extensibility.

New providers can be written which bridge other languages (e.g.: Python, etc...) to the data model. Such would be presently encapsulated in legacy debugger extensions for loading purposes. The script provider itself should minimize the dependency with legacy engine interfaces and should only utilize the data model APIs where possible. This will allow the provider to be made portable to other environments with significantly greater ease.

There are two classes of interfaces related to script providers. The first class of interfaces is for general management of script providers and the scripts they manage. The second class of interfaces is for support of script debugging. While support for the first set is mandatory, support for the second is optional and may not make sense for every provider. 


The general management interfaces are: 

Interface | Description
|---------|------------|
IDataModelScriptProvider | The core interface that a script provider must implement. This is the interface which is registered with the script manager portion of the data model manager in order to advertise the provider's support of a particular type of script and register against a particular file extension
IDataModelScript | An abstraction of a particular script which is being managed by the provider. Each script which is loaded or being edited has a separate IDataModelScript instance
IDataModelScriptClient | A client interface which is used by the script provider in order to communicate information to a user interface. Script providers do not implement this interface. The application hosting the data model which wishes to make use of script providers does. A script provider will call into methods of the script client to report status, errors, etc...
IDataModelScriptHostContext | A host interface which is used by the script provider as a container for the contents of the script. How the contents of a script surface other than the manipulations that it performs to the object model of the debugger application is up to the particular debug host. This interface allows the script provider to get information about where to place its contents.
IDataModelScriptTemplate | Script providers can provide one or more templates which serve as starting points for users to author scripts. A debugger application which provides a built-in editor can prefill new scripts with template content as advertised by the provider through this interface.
IDataModelScriptTemplateEnumerator | An enumerator interface that the script provider implements in order to advertise all the various templates it supports.
IDataModelNameBinder | A name binder -- an object which can associate a name in a context with a value. For a given expression such as "foo.bar", a name binder is able to bind the name "bar" in the context of object "foo" and produce a value or reference to it. Name binders are not typically implemented by a script provider; rather, the default binder can be acquired from the data model and used by the script provider

The debug interfaces are: 

Interface | Description
|---------|------------|
IDataModelScriptDebug | The core interface that a script provider must provide in order to make a script debuggable. The implementation class of the IDataModelScript interface must QueryInterface for IDataModelScriptDebug if the script is debuggable.
IDataModelScriptDebugClient | The user interface which wishes to provide the capability of script debugging implements the IDataModelScriptDebugClient interface. The script provider utilizes this interface to pass debug information back and forth (e.g.: events which occur, breakpoints, etc...)
IDataModelScriptDebugStack | The script provider implements this interface to expose the notion of a call stack to the script debugger.
IDataModelScriptDebugStackFrame | The script provider implements this interface to expose the notion of a particular stack frame within the call stack.
IDataModelScriptDebugVariableSetEnumerator | The script provider implements this interface to expose a set of variables. This set may represent the set of parameters to a function, the set of local variables, or the set of variables within a particular scope. The exact meaning is dependent upon how the interface was acquired.
IDataModelScriptDebugBreakpoint | The script provider implements this interface to expose the notion of and control of a particular breakpoint within the script.
IDataModelScriptDebugBreakpointEnumerator | The script provider implements this to enumerate all of the breakpoints which currently exist within the script (whether enabled or not).

**The Core Script Provider: IDataModelScriptProvider**

Any extension which wants to be a script provider must provide an implementation of the IDataModelScriptProvider interface and register such with the script manager portion of the data model manager via the RegisterScriptProvider method. This core interface which must be implemented is defined as follows.

```cpp 
DECLARE_INTERFACE_(IDataModelScriptProvider, IUnknown)
{
    STDMETHOD(GetName)(_Out_ BSTR *name) PURE;
    STDMETHOD(GetExtension)(_Out_ BSTR *extension) PURE;
    STDMETHOD(CreateScript)(_COM_Outptr_ IDataModelScript **script) PURE;
    STDMETHOD(GetDefaultTemplateContent)(_COM_Outptr_ IDataModelScriptTemplate **templateContent) PURE;
    STDMETHOD(EnumerateTemplates)(_COM_Outptr_ IDataModelScriptTemplateEnumerator **enumerator) PURE;
}
```

[GetName](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptprovider-getname)

The GetName method returns the name of the type of (or language of) scripts which the provider manages as a string allocated via the SysAllocString method. The caller is responsible for freeing the returned string via SysFreeString. Examples of strings which might be returned from this method are "JavaScript" or "NatVis". The returned string is likely to appear in the user interface of the debugger application which is hosting the data model. 
No two script providers may return the same name (case insensitive). 

[GetExtension](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptprovider-getextension)

The GetExtension method returns the file extension for scripts managed by this provider (without the dot) as a string allocated via the SysAllocString method. The debugger application hosting the data model (with scripting support) will delegate opening of script files with this extension to the script provider. The caller is responsible for freeing the returned string via SysFreeString. Examples of strings which might be returned from this method are "js" or "NatVis". 

[CreateScript](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptprovider-createscript)

The CreateScript method is called to create a new script. The script provider must return a new and empty script represented by the returned IDataModelScript interface whenever this method is called. Note that this method is called regardless of whether a user interface is creating a new blank script for editing by the user or whether the debugger application is loading a script from disk. The provider does not get involved in file I/O. It merely handles the requests from the hosting application via streams passed to methods on IDataModelScript. 

[GetDefaultTemplateContent](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptprovider-getdefaulttemplatecontent)

The GetDefaultTemplateContent method returns an interface for the default template content of the provider. This is content that the script provider would like pre-populated in an edit window for a newly created script. If the script provider has no templates (or has no template content which is designated as the default content), the script provider may return E_NOTIMPL from this method. 

[EnumerateTemplates](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptprovider-enumeratetemplates)

The EnumerateTemplates method returns an enumerator which is capable of enumerating the variety of templates that are provided by the script provider. Template content is what the script provider wants to be "prefilled" into an edit window when creating a new script. If there are multiple different templates supported, those templates can be named (e.g.: "Imperative Script", "Extension Script") and the debugger application hosting the data model can choose how to present the "templates" to the user. 


**The Core Script Interface: IDataModelScript**

The main interface which manages an individual script that is implemented by the provider is the IDataModelScript interface. A component implementing this interface is returned when the client wishes to create a new blank script and calls the CreateScript method on IDataModelScriptProvider. 

Each script which is created by the provider should be in an independent silo. One script should not be able to impact another script except through explicit interaction with external objects via the data model. Two scripts, can for instance, both extend some type or concept (e.g.: the debugger's notion of what a process is). Either script can then access each other's fields via the external process object. 

The interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScript, IUnknown)
{
    STDMETHOD(GetName)(_Out_ BSTR *scriptName) PURE;
    STDMETHOD(Rename)(_In_ PCWSTR scriptName) PURE;
    STDMETHOD(Populate)(_In_ IStream *contentStream) PURE;
    STDMETHOD(Execute)(_In_ IDataModelScriptClient *client) PURE;
    STDMETHOD(Unlink)() PURE;
    STDMETHOD(IsInvocable)(_Out_ bool *isInvocable) PURE;
    STDMETHOD(InvokeMain)(_In_ IDataModelScriptClient *client) PURE; 
}
```

[GetName](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-getname)

The GetName method returns the name of the script as an allocated string via the SysAllocString function. If the script does not yet have a name, the method should return a null BSTR. It should not fail in this circumstance. If the script is explicitly renamed via a call to the Rename method, the GetName method should return the newly assigned name. 

[Rename](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-rename)

The Rename method assigns a new name to the script. It is the responsibility of the script implementation to save this name and return it upon any call to the GetName method. This is often called when a user interface chooses to Save As the script to a new name. Note that renaming the script may affect where the hosting application chooses to project the contents of the script. 

[Populate](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-populate)

The Populate method is called by the client in order to change or synchronize the "content" of the script. It is the notification that is made to the script provider that the code of the script has changed. It is important to note that this method does not cause execution of the script or changes to any of the objects that the script manipulates. This is merely a notification to the script provider that the content of the script has changed so that it may synchronize its own internal state. 

[Execute](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-execute)

The Execute method executes the content of the script as dictated by the last successful Populate call and modifies the object model of the debugger according to that content. If the language (or the script provider) defines a "main function" -- one that the author would want called upon clicking an imaginary "Execute Script" button in a user interface -- such "main function" is not called during an Execute operation. The Execute operation can be considered to perform initialization and object model manipulations only (e.g.: executing root code and setting up extensibility points). 

[Unlink](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-unlink)

The Unlink method undoes the Execute operation. Any object model manipulations or extensibility points established during the execution of the script are undone. After an Unlink operation, the script may be re-executed via a call to Execute or it may be released. 

[IsInvocable](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-isinvocable)

The IsInvocable method returns whether or not the script is invocable -- that is, whether it has a "main function" as defined by its language or provider. Such a "main function" is conceptually something that the script author would want called if an imaginary "Execute Script" button were pressed in a user interface. 

[InvokeMain](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscript-invokemain)

If the script has a "main function" which is intended to execute from a UI invocation, it indicates such via a true return from the IsInvocable method. The user interface can then call the InvokeMain method to actually "invoke" the script. Note that this is distinct from *Execute* which runs all root code and bridges the script to the namespace of the underlying host. 


**The Script Client: IDataModelScriptClient **

An application hosting the data model that wants to manage scripts and have a user interface (whether graphical or console) around this notion implements the IDataModelScriptClient interface. This interface is passed to any script provider during execution or invocation or a script in order to pass error and event information back to the user interface. 

The IDataModelScriptClient interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptClient, IUnknown)
{
   STDMETHOD(ReportError)(_In_ ErrorClass errClass, _In_ HRESULT hrFail, _In_opt_ PCWSTR message, _In_ ULONG line, _In_ ULONG position) PURE;
}
```

[ReportError](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptclient-reporterror)

If an error occurs during execution or invocation of the script, the script provider calls the ReportError method to notify the user interface of the error. 


**The Host Context for a Script: IDataModelScriptHostContext**

The debug host has some influence over how and where it projects data model script content. It is expected that each script ask the host for a context in which to place bridges to the script (e.g.: function objects that can be called, etc...). This context is retrieved via calling the CreateContext method on IDebugHostScriptHost and getting an IDataModelScriptHostContext. 

The IDataModelScriptHostContext interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptHostContext, IUnknown)
{
   STDMETHOD(NotifyScriptChange)(_In_ IDataModelScript* script, _In_ ScriptChangeKind changeKind) PURE;
   STDMETHOD(GetNamespaceObject)(_COM_Outptr_ IModelObject** namespaceObject) PURE;
}
```

[NotifyScriptChange](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripthostcontext-notifyscriptchange)

It is required that a script provider notify the debug host upon certain operations occurring with a method call to the NotifyScriptChange method on the associated context. Such operations are defined as members of the ScriptChangeKind enumeration

[GetNamespaceObject](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripthostcontext-getnamespaceobject)

The GetNamespaceObject method returns an object into which the script provider can place any bridges between the data model and the script. It is here, for instance, that the script provider might place data model method objects (IModelMethod interfaces boxed into IModelObject) whose implementation calls into correspondingly named functions in the script. 


**Templates for Newly Created Scripts: IDataModelScriptTemplate**

Script providers that want to present pre-filled content for new scripts (e.g.: to aid users writing scripts in a debugger user interface) can do so by providing one or more script templates. Such templates are components which implement the IDataModelScriptTemplate interface and are returned via either the GetDefaultTemplate method or EnumerateTemplates method on the script provider. 

The IDataModelScriptTemplate interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptTemplate, IUnknown)
{
   STDMETHOD(GetName)(_Out_ BSTR *templateName) PURE;
   STDMETHOD(GetDescription)(_Out_ BSTR *templateDescription) PURE;
   STDMETHOD(GetContent)(_COM_Outptr_ IStream **contentStream) PURE;
}
```


[GetName](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripttemplate-getname)

The GetName method returns a name of the template. This may fail with E_NOTIMPL if the template does not have a name. The single default template (if such exists) is not required to have a name. All other templates are. These names may be presented in a user interface as part of a menu to select which template is to be created. 


[GetDescription](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripttemplate-getdescription)

The GetDescription method returns a description of the template. Such description would be presented to the user in more descriptive interfaces to help the user understand what the template is designed to do. The template may return E_NOTIMPL from this method if it does not have a description. 

[GetContent](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripttemplate-getcontent)

The GetContent method returns the content (or code) of the template. This is what would be pre-filled into the edit window if a user elected to create a new script from this template. The template is responsible for creating (and returning) a standard stream over the content that the client can pull. 

**Enumeration of a Provider's Template Content: IDataModelScriptTemplateEnumerator**

A script provider can provide one or more templates which pre-fill content into newly created scripts in some user interface. If any of these templates are provided, the script provider must implement an enumerator over them which is returned upon a call to the EnumerateTemplates method. 

Such enumerator is an implementation of the IDataModelScriptTemplateEnumerator interface and is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptTemplateEnumerator, IUnknown)
{
   STDMETHOD(Reset)() PURE;
   STDMETHOD(GetNext)(_COM_Outptr_ IDataModelScriptTemplate **templateContent) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripttemplateenumerator-reset)

The Reset method resets the enumerator to the position it was at when it was first created -- before the first template produced. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscripttemplateenumerator-getnext)

The GetNext method moves the enumerator to the next template and returns it. At the end of enumeration, the enumerator returns E_BOUNDS. Once the E_BOUNDS marker has been hit, the enumerator will continue to produce E_BOUNDS errors indefinitely until a Reset call is made. 


**Resolving the Meaning of Names: IDataModelNameBinder**

The data model provides a standard way for script providers to determine the meaning of a given name in a given context (e.g.: determining what bar means for foo.bar) that will operate across a variety of script providers. This mechanism is known as a name binder and is represented by the IDataModelNameBinder interface. Such a binder encapsulates a set of rules about how the name resolves and how to deal with conflict resolution where a name is defined multiple times on an object. Part of these rules include things such as how a projected name (one added by a data model) resolves against a native name (one in the type system of the language being debugged). 

In order to provide a degree of consistency across script providers, the data model's script manager provides a default name binder'. This default name binder can be acquired via a call to the GetDefaultNameBinder method on the IDataModelScriptManager interface. The name binder interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelNameBinder, IUnknown)
{
   STDMETHOD(BindValue)(_In_ IModelObject* contextObject, _In_ PCWSTR name, _COM_Errorptr_ IModelObject** value, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(BindReference)(_In_ IModelObject* contextObject, _In_ PCWSTR name, _COM_Errorptr_ IModelObject** reference, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(EnumerateValues)(_In_ IModelObject* contextObject, _COM_Outptr_ IKeyEnumerator** enumerator) PURE;
   STDMETHOD(EnumerateReferences)(_In_ IModelObject* contextObject, _COM_Outptr_ IKeyEnumerator** enumerator) PURE;
}
```

[BindValue](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelnamebinder-bindvalue)

The BindValue method performs the equivalent of contextObject.name on the given object according to a set of binding rules. The result of this binding is a value. As a value, the underlying script provider cannot use the value to perform assignment back to name.

[BindReference](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelnamebinder-bindreference)

The BindReference method is similar to BindValue in that it also performs the equivalent of contextObject.name on the given object according to a set of binding rules. The result of the binding from this method is, however, a reference instead of a value. As a reference, the script provider can utilize the reference to perform assignment back to name. 

[EnumerateValues](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelnamebinder-enumeratevalues)

The EnumerateValues method enumerates the set of names and values which will bind against the object according to the rules of the BindValue method. Unlike the EnumerateKeys, EnumerateValues, and similar methods on IModelObject which may return multiple names with the same value (for base classes, parent models, and the like), this enumerator will only return the specific set of names which will bind with BindValue and BindReference. Names will never be duplicated. Note that there is a significantly higher cost of enumerating an object via the name binder than calling the IModelObject methods. 

[EnumerateReferences](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelnamebinder-enumeratereferences)

The EnumerateReferences method enumerates the set of names and references to them which will bind against the object according to the rules of the BindReference method. Unlike the EnumerateKeys, EnumerateValues, and similar methods on IModelObject which may return multiple names with the same value (for base classes, parent models, and the like), this enumerator will only return the specific set of names which will bind with BindValue and BindReference. Names will never be duplicated. Note that there is a significantly higher cost of enumerating an object via the name binder than calling the IModelObject methods. 


## <span id="debugscript"> Debugger Data Model C++ Script Debugging Interfaces

The infrastructure for script providers in the data model also provides a concept around debugging scripts. Any script that wishes to expose debugging capabilities to the debug host and the debugger application hosting the data model can do so by having debuggable scripts implement the IDataModelScriptDebug interface in addition to the IDataModelScript interface. The presence of this interface on the script indicates to the infrastructure that it is debuggable. 

While the IDataModelScriptDebug interface is the starting point to get access to the debug capabilities of a script provider, it is joined by a set of other interfaces in providing overall debug capabilities. 

The debug interfaces are: 

Interface | Description
|---------|------------|
IDataModelScriptDebug | The core interface that a script provider must provide in order to make a script debuggable. The implementation class of the IDataModelScript interface must QueryInterface for IDataModelScriptDebug if the script is debuggable.
IDataModelScriptDebugClient | The user interface which wishes to provide the capability of script debugging implements the IDataModelScriptDebugClient interface. The script provider utilizes this interface to pass debug information back and forth (e.g.: events which occur, breakpoints, etc...)
IDataModelScriptDebugStack | The script provider implements this interface to expose the notion of a call stack to the script debugger.
IDataModelScriptDebugStackFrame | The script provider implements this interface to expose the notion of a particular stack frame within the call stack.
IDataModelScriptDebugVariableSetEnumerator | The script provider implements this interface to expose a set of variables. This set may represent the set of parameters to a function, the set of local variables, or the set of variables within a particular scope. The exact meaning is dependent upon how the interface was acquired.
IDataModelScriptDebugBreakpoint | The script provider implements this interface to expose the notion of and control of a particular breakpoint within the script.
IDataModelScriptDebugBreakpointEnumerator | The script provider implements this to enumerate all of the breakpoints which currently exist within the script (whether enabled or not).

The general management interfaces are: 

Interface | Description
|---------|------------|
IDataModelScriptProvider | The core interface that a script provider must implement. This is the interface which is registered with the script manager portion of the data model manager in order to advertise the provider's support of a particular type of script and register against a particular file extension
IDataModelScript | An abstraction of a particular script which is being managed by the provider. Each script which is loaded or being edited has a separate IDataModelScript instance
IDataModelScriptClient | A client interface which is used by the script provider in order to communicate information to a user interface. Script providers do not implement this interface. The application hosting the data model which wishes to make use of script providers does. A script provider will call into methods of the script client to report status, errors, etc...
IDataModelScriptHostContext | A host interface which is used by the script provider as a container for the contents of the script. How the contents of a script surface other than the manipulations that it performs to the object model of the debugger application is up to the particular debug host. This interface allows the script provider to get information about where to place its contents.
IDataModelScriptTemplate | Script providers can provide one or more templates which serve as starting points for users to author scripts. A debugger application which provides a built-in editor can prefill new scripts with template content as advertised by the provider through this interface.
IDataModelScriptTemplateEnumerator | An enumerator interface that the script provider implements in order to advertise all the various templates it supports.
IDataModelNameBinder | A name binder -- an object which can associate a name in a context with a value. For a given expression such as "foo.bar", a name binder is able to bind the name "bar" in the context of object "foo" and produce a value or reference to it. Name binders are not typically implemented by a script provider; rather, the default binder can be acquired from the data model and used by the script provider.


**Making Scripts Debuggable: IDataModelScriptDebug**

Any script which is debuggable indicates this capability via the presence of the IDataModelScriptDebug interface on the same component which implements IDataModelScript. The query for this interface by the debug host or the debugger application hosting the data model is what indicates the presence of the debug capability. 

The IDataModelScriptDebug interface is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebug, IUnknown)
{
   STDMETHOD_(ScriptDebugState, GetDebugState)() PURE;
   STDMETHOD(GetCurrentPosition)(_Out_ ScriptDebugPosition *currentPosition, _Out_opt_ ScriptDebugPosition *positionSpanEnd, _Out_opt_ BSTR *lineText) PURE;
   STDMETHOD(GetStack)(_COM_Outptr_ IDataModelScriptDebugStack **stack) PURE;
   STDMETHOD(SetBreakpoint)(_In_ ULONG linePosition, _In_ ULONG columnPosition, _COM_Outptr_ IDataModelScriptDebugBreakpoint **breakpoint) PURE;
   STDMETHOD(FindBreakpointById)(_In_ ULONG64 breakpointId, _COM_Outptr_ IDataModelScriptDebugBreakpoint **breakpoint) PURE;
   STDMETHOD(EnumerateBreakpoints)(_COM_Outptr_ IDataModelScriptDebugBreakpointEnumerator **breakpointEnum) PURE;
   STDMETHOD(GetEventFilter)(_In_ ScriptDebugEventFilter eventFilter, _Out_ bool *isBreakEnabled) PURE;
   STDMETHOD(SetEventFilter)(_In_ ScriptDebugEventFilter eventFilter, _In_ bool isBreakEnabled) PURE;
   STDMETHOD(StartDebugging)(_In_ IDataModelScriptDebugClient *debugClient) PURE;
   STDMETHOD(StopDebugging)(_In_ IDataModelScriptDebugClient *debugClient) PURE;
}
```

[GetDebugState](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-getdebugstate)

The GetDebugState method returns the current state of the script (e.g.: whether it is executing or not). The state is defined by a value within the ScriptDebugState enumeration.

[GetCurrentPosition](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-getcurrentposition)

The GetCurrentPosition' method returns the current position within the script. This may only be called when the script is broken into the debugger where a call to GetScriptState would return ScriptDebugBreak. Any other call to this method is invalid and will fail. 

[GetStack](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-getstack)

The GetStack method gets the current call stack at the break position. This method may only be called when the script is broken into the debugger. 

[SetBreakpoint](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-setbreakpoint)

The SetBreakpoint method sets a breakpoint within the script. Note that the implementation is free to adjust the inpassed line and column positions to move forward to an appropriate code position. The actual line and column numbers where the breakpoint was placed can be retrieved by method calls on the returned IDataModelScriptDebugBreakpoint interface. 

[FindBreakpointById](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-findbreakpointbyid)

Each breakpoint which is created within the script via the SetBreakpoint method is assigned a unique identifier (a 64-bit unsigned integer) by the implementation. The FindBreakpointById method is used to get an interface to the breakpoint from a given identifier. 

[EnumerateBreakpoints](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-enumeratebreakpoints)

The EnumerateBreakpoints method returns an enumerator capable of enumerating every breakpoint which is set within a particular script. 

[GetEventFilter](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-geteventfilter)

The GetEventFilter method returns whether "break on event" is enabled for a particular event. Events which can cause "break on event" are described by a member of the ScriptDebugEventFilter enumeration. 

[SetEventFilter](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-seteventfilter)

The SetEventFilter method changes the "break on event" behavior for a particular event as defined by a member of the ScriptDebugEventFilter enumeration. A full list of available events (and a description of this enumeration) can be found in the documentation for the GetEventFilter method. 

[StartDebugging](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-startdebugging)

The StartDebugging method "turns on" the debugger for a particular script. The act of starting debugging does not actively cause any execution break or stepping. It merely makes the script debuggable and provides a set of interfaces for the client to communicate with the debugging interface. 

[StopDebugging](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebug-stopdebugging)

The StopDebugging method is called by a client that wants to stop debugging. This method call may be made at any point after StartDebugging was made successfully (e.g.: during a break, while the script is executing, etc...). The call immediately ceases all debugging activity and resets the state back to before StartDebugging was called. 


**The Debugging Interface: IDataModelScriptDebugClient**

The debug host or debugger application which wishes to provide an interface around script debugging must provide an implementation of the IDataModelScriptDebugClient interface to the script debugger via the StartDebugging method on the debug interface for the script. 

The IDataModelScriptDebugClient is the communication channel across which debug events are passed and control goes from the script execution engine to a debugger interface. It is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugClient, IUnknown)
{
   STDMETHOD(NotifyDebugEvent)(_In_ ScriptDebugEventInformation *pEventInfo, _In_ IDataModelScript *pScript, _In_opt_ IModelObject *pEventDataObject, _Inout_ ScriptExecutionKind *resumeEventKind) PURE;
}
```

[NotifyDebugEvent](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugclient-notifydebugevent)

Whenever any event occurs which breaks into the script debugger, the debug code itself makes a call to the interface via the NotifyDebugEvent method. This method is synchronous. No execution of the script will resume until the interface returns from the event. The definition of the script debugger is intended to be simple: there are absolutely no nested events requiring processing. 
A debug event is defined by a variant record known as a ScriptDebugEventInformation. Which fields in the event information are valid is largely defined by the DebugEvent member. It defines the kind of event which occurred as described by a member of the ScriptDebugEvent enumeration.

**The Call Stack: IDataModelScriptDebugStack**

When an event occurs which breaks into the script debugger, the debugging interface will want to retrieve the call stack for the break location. This is done through the GetStack method. Such stack is expressed via the IDataModelScriptDebugStack which is defined as indicated below. 

Note that the overall stack may span multiple scripts and/or multiple script providers. The call stack which is returned from a single call to the GetStack method on a particular script's debug interface should only return the segment of the call stack within the bounds of that script. It is entirely possible that a script debug engine can retrieve the call stack as spans multiple script contexts if two scripts of the same provider interact. The GetStack method should not return the portion of the stack which is in another script. Instead, if this situation can be detected, the stack frame which is the boundary frame into the script should mark itself as a transition frame via an implementation of the IsTransitionPoint and GetTransition methods on that stack frame. It is expected that the debugger interface will stitch together the overall stack from the multiple stack segments which exist. 

It is imperative that transitions be implemented in this manner or the debug interface may direct inquiries about local variables, parameters, breakpoints, and other script specific constructs to the wrong script context! This will result in undefined behavior in the debugger interface. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugStack, IUnknown)
{
   STDMETHOD_(ULONG64, GetFrameCount)() PURE;
   STDMETHOD(GetStackFrame)(_In_ ULONG64 frameNumber, _COM_Outptr_ IDataModelScriptDebugStackFrame **stackFrame) PURE;
}
```

[GetFrameCount](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstack-getframecount)

The GetFrameCount method returns the number of stack frames in this segment of the call stack. If the provider can detect frames in different script contexts or of different providers, it should indicate this to the caller by implementation of the IsTransitionPoint and GetTransition methods on the entry frame into this stack segment. 

[GetStackFrame](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstack-getstackframe)

The GetStackFrame gets a particular stack frame from the stack segment. The call stack has a zero based indexing system: the current stack frame where the break event occurred is frame 0. The caller of the current method is frame 1 (and so forth). 


**Examining State When Broken: IDataModelScriptDebugStackFrame**

A particular frame of the call stack when broken into the script debugger can be retrieved via a call to the GetStackFrame method on the IDataModelScriptDebugStack interface representing the stack segment where the break occurred. The IDataModelScriptDebugStackFrame interface which is returned to represent this frame is defined as follows.

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugStackFrame, IUnknown)
{
   STDMETHOD(GetName)(_Out_ BSTR *name) PURE;
   STDMETHOD(GetPosition)(_Out_ ScriptDebugPosition *position, _Out_opt_ ScriptDebugPosition *positionSpanEnd, _Out_opt_ BSTR *lineText) PURE;
   STDMETHOD(IsTransitionPoint)(_Out_ bool *isTransitionPoint) PURE;
   STDMETHOD(GetTransition)(_COM_Outptr_ IDataModelScript **transitionScript, _Out_ bool *isTransitionContiguous) PURE;
   STDMETHOD(Evaluate)(_In_ PCWSTR pwszExpression, _COM_Outptr_ IModelObject **ppResult) PURE;
   STDMETHOD(EnumerateLocals)(_COM_Outptr_ IDataModelScriptDebugVariableSetEnumerator **variablesEnum) PURE;
   STDMETHOD(EnumerateArguments)(_COM_Outptr_ IDataModelScriptDebugVariableSetEnumerator **variablesEnum) PURE;
}
```

[GetName](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-getname)

The GetName method returns the display name (e.g.: function name) of this frame. Such name will be displayed within the stack backtrace presented to the user in the debugger interface. 

[GetPosition](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-getposition)

The GetPosition method returns the position within the script represented by the stack frame. This method may only be called when the script is within a break represented by the stack in which this frame is contained. The line and column position within this frame is always returned. If the debugger is capable of returning the span of the "execution position" within the script, an ending position can be returned in the positionSpanEnd argument. If the debugger is not capable of this, the line and column values in the span end (if requested) should be set to zero. 

[IsTransitionPoint](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-istransitionpoint)

The IDataModelScriptDebugStack interface represents a segment of a call stack -- that portion of the call stack which is contained within the context of one script. If the debugger is capable of detecting the transition from one script to another (or one script provider to another), it can indicate this by implementing the IsTransitionPoint method and returning true or false as appropriate. The call stack frame which entered the script where the segment applies should be considered a transition point. All other frames are not. 

[GetTransition](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-gettransition)

If a given stack frame is a transition point as determined by the IsTransition method (see the documentation there for a definition of transition points), the GetTransition method returns information about the transition. In particular, this method returns the previous script -- the one which made a call into the script represented by the stack segment containing this IDataModelScriptDebugStackFrame. 

[Evaluate](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-evaluate)

The Evaluate method evaluates an expression (of the language of the script provider) in the context of the stack frame represented by the IDataModelScriptDebugStackFrame interface on which this method was called. The result of the expression evaluation must be marshaled out of the script provider as an IModelObject. The properties and other constructs on the resulting IModelObject must all be able to be acquired while the debugger is in a break state. 

[EnumerateLocals](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-enumeratelocals)

The EnumerateLocals method returns a variable set (represented by an IDataModelScriptDebugVariableSetEnumerator interface) for all local variables which are in scope in the context of the stack frame represented by the IDataModelScriptDebugStackFrame interface on which this method was called. 

[EnumerateArguments](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugstackframe-enumeratearguments)

The EnumerateArguments method returns a variable set (represented by an IDataModelScriptDebugVariableSetEnumerator interface) for all function arguments of the function called in the stack frame represented by the IDataModelScriptDebugStackFrame interface on which this method was called. 


**Looking at Variables: IDataModelScriptDebugVariableSetEnumerator**

A set of variables in the script being debugged (whether those in a particular scope, the locals of a function, the arguments of a function, etc...) is represented by a variable set defined through the IDataModelScriptDebugVariableSetEnumerator interface:

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugVariableSetEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_Out_ BSTR *variableName, _COM_Outptr_opt_ IModelObject **variableValue, _COM_Outptr_opt_result_maybenull_ IKeyStore **variableMetadata) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugvariablesetenumerator-reset)

The Reset method resets the position of the enumerator to where it was immediately after creation -- that is, before the first element of the set. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugvariablesetenumerator-getnext)

The GetNext method moves the enumerator to the next variable in the set and returns the variable's name, value, and any metadata associated with it. If the enumerator has hit the end of the set, the error E_BOUNDS is returned. Once the E_BOUNDS marker has been returned from the GetNext method, it will continue to produce E_BOUNDS when called again unless an intervening Reset call is made. 


**Breakpoints: IDataModelScriptDebugBreakpoint**

Script breakpoints are set via the SetBreakpoint method on a given script's debug interface. Such breakpoints are represented both by a unique id and an implementation of the IDataModelScriptDebugBreakpoint interface which is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugBreakpoint, IUnknown)
{
    STDMETHOD_(ULONG64, GetId)() PURE;
    STDMETHOD_(bool, IsEnabled)() PURE;
    STDMETHOD_(void, Enable)() PURE;
    STDMETHOD_(void, Disable)() PURE;
    STDMETHOD_(void, Remove)() PURE;
    STDMETHOD(GetPosition)(_Out_ ScriptDebugPosition *position, _Out_opt_ ScriptDebugPosition *positionSpanEnd, _Out_opt_ BSTR *lineText) PURE;
}
```

[GetId](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-getid)

The GetId method returns the unique identifier assigned by the script provider's debug engine to the breakpoint. This identifier must be unique within the context of the containing script. The breakpoint identifier may be unique to the provider; however, that is not required. 

[IsEnabled](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-isenabled)

The IsEnabled method returns whether or not the breakpoint is enabled. A disabled breakpoint still exists and is still in the list of breakpoints for the script, it is merely "turned off" temporarily. All breakpoints should be created in the enabled state. 

[Enable](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-enable)

The Enable method enables the breakpoint. If the breakpoint was disabled, "hitting the breakpoint" after calling this method will cause a break into the debugger. 

[Disable](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-disable)

The Disable method disables the breakpoint. After this call, "hitting the breakpoint" after calling this method will not break into the debugger. The breakpoint, while still present, is considered "turned off". 

[Remove](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-remove)

The Remove method removes the breakpoint from its containing list. The breakpoint no longer semantically exists after this method returns. The IDataModelScriptDebugBreakpoint interface which represented the breakpoint is considered orphaned after the call. Nothing else can (legally) be done with it after this call other than releasing it. 

[GetPosition](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpoint-getposition)

The GetPosition method returns the position of the breakpoint within the script. The script debugger must return the line and column within source code where the breakpoint is located. If it is capable of doing so, it can also return a span of source represented by the breakpoint by filling out an end position as defined by the positionSpanEnd argument. If the debugger is not capable of producing this span and the caller requests it, the Line and Column fields of the span's ending position should be filled in as zero indicating that the values cannot be provided. 


**Breakpoint Enumeration: IDataModelScriptDebugBreakpointEnumerator**

If a script provider supports debugging, it must also keep track of all breakpoints associated with each and every script and be capable of enumerating those breakpoints to the debug interface. The enumerator for breakpoints is acquired via the EnumerateBreakpoints method on the debug interface for a given script and is defined as follows. 

```cpp
DECLARE_INTERFACE_(IDataModelScriptDebugBreakpointEnumerator, IUnknown)
{
   STDMETHOD(Reset)() PURE;
   STDMETHOD(GetNext)(_COM_Outptr_ IDataModelScriptDebugBreakpoint **breakpoint) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpointenumerator-reset)

The Reset method resets the position of the enumerator to where it was just after the enumerator was created -- that is, before the first enumerated breakpoint. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-idatamodelscriptdebugbreakpointenumerator-getnext)

The GetNext method moves the enumerator forward to the next breakpoint to be enumerated and returns the IDataModelScriptDebugBreakpoint interface for that breakpoint. If the enumerator has reached the end of the enumeration, it returns E_BOUNDS. Once the E_BOUNDS error has been produced, subsequent calls to the GetNext method will continue to produce E_BOUNDS unless an intervening call to the Reset method has been made. 

---

## <span id="related_topics"></span>See also

This topic is part of a series which describes the interfaces accessible from C++, how to use them to build a C++ based debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.

[Debugger Data Model C++ Overview](data-model-cpp-overview.md)

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)
