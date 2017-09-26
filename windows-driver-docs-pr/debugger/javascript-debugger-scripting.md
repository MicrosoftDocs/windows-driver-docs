---
title: JavaScript Debugger Scripting
description: This topic describes how to use JavaScript to create scripts that understand debugger objects and extend and customize the capabilities of the debugger.
ms.assetid: 3442E2C4-4054-4698-B7FB-8FE19D26C171
---

# JavaScript Debugger Scripting


This topic describes how to use JavaScript to create scripts that understand debugger objects and extend and customize the capabilities of the debugger.

## <span id="Overview_of_JavaScript_Debugger_Scripting_"></span><span id="overview_of_javascript_debugger_scripting_"></span><span id="OVERVIEW_OF_JAVASCRIPT_DEBUGGER_SCRIPTING_"></span>Overview of JavaScript Debugger Scripting


Script providers bridge a scripting language to the debugger's internal object model. The JavaScript debugger scripting provider, allows the for use of JavaScript with the debugger.

When a JavaScript is loaded via the .scriptload command, the root code of the script is executed, the names which are present in the script are bridged into the root namespace of the debugger (dx Debugger) and the script stays resident in memory until it is unloaded and all references to its objects are released. The script can provide new functions to the debugger's expression evaluator, modify the object model of the debugger, or can act as a visualizer in much the same way that a NatVis visualizer does.

This topic describes some of what you can do with JavaScript debugger scripting.

[Load The Debugger JavaScript Provider](#provider)

[Use the JavaScript Scripting Meta Commands](#commands)

[Get Started with JavaScript Debugger Scripting](#started)

[Automate Debugger Commands](#automate)

[Set Conditional Breakpoints with JavaScript](#breakpoints)

[Create a Debugger Visualizer in JavaScript](#visualizer)

[Work With 64-Bit Values in JavaScript Extensions](#bitvalues)

[JavaScript Resources](#resources)

These two topics provide additional information about working with JavaScript in the debugger.

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

## <span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>The Debugger JavaScript Provider


The JavaScript provider included with the debugger takes full advantage of the latest ECMAScript6 object and class enhancements. For more information, see [ECMAScript 6 — New Features: Overview & Comparison](http://es6-features.org/).

**JsProvider.dll**

JsProvider.dll is the JavaScript provider that is loaded to support JavaScript Debugger Scripting.

**Requirements**

JavaScript Debugger Scripting is designed to work with all supported versions of Windows.

## <span id="Loading_the_JavaScript_Scripting_Provider"></span><span id="loading_the_javascript_scripting_provider"></span><span id="LOADING_THE_JAVASCRIPT_SCRIPTING_PROVIDER"></span>Loading the JavaScript Scripting Provider


Before using any of the .script commands, a scripting provider needs to be loaded using the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command. To load the JavaScript provider, use the following command.

```
0:000> .load jsprovider.dll
```

Use the .scriptproviders command to confirm that the JavaScript provider is loaded.

```
0:000> .scriptproviders
Available Script Providers:
    NatVis (extension '.NatVis')
    JavaScript (extension '.js')
```

## <span id="Commands"></span><span id="commands"></span><span id="COMMANDS"></span>JavaScript Scripting Meta Commands


The following commands are available to work with JavaScript Debugger Scripting.

-   [**.scriptproviders (List Script Providers)**](-scriptproviders--list-script-providers-.md)
-   [**.scriptload (Load Script)**](-scriptload--load-script-.md)
-   [**.scriptunload (Unload Script)**](-scriptunload--unload-script-.md)
-   [**.scriptrun (Run Script)**](-scriptrun--run-script-.md)
-   [**.scriptlist (List Loaded Scripts)**](-scriptlist--list-loaded-scripts-.md)

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded using the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command. To load the JavaScript provider, use the following command.

```
0:000> .load jsprovider.dll
```

## <span id=".scriptproviders__list_script_providers_"></span><span id=".SCRIPTPROVIDERS__LIST_SCRIPT_PROVIDERS_"></span>.scriptproviders (List Script Providers)


The .scriptproviders command will list all the script languages which are presently understood by the debugger and the extension under which they are registered.

In the example below, the JavaScript and NatVis providers are loaded.

```
0:000> .scriptproviders
Available Script Providers:
    NatVis (extension '.NatVis')
    JavaScript (extension '.js')
```

Any file ending in ".NatVis" is understood as a NatVis script and any file ending in ".js" is understood as a JavaScript script. Either type of script can be loaded with the .scriptload command.

For more information, see [**.scriptproviders (List Script Providers)**](-scriptproviders--list-script-providers-.md)

## <span id=".scriptload__load_script_"></span><span id=".SCRIPTLOAD__LOAD_SCRIPT_"></span>.scriptload (Load Script)


The .scriptload command will load a script and execute the root code of a script and the *initializeScript* function. If there are any errors in the initial load and execution of the script, the errors will be displayed to console. The following command shows the successful load of TestScript.js.

```
0:000> .scriptload C:\WinDbg\Scripts\TestScript.js
JavaScript script successfully loaded from 'C:\WinDbg\Scripts\TestScript.js'
```

Any object model manipulations made by the script will stay in place until the script is subsequently unloaded or is run again with different content.

For more information, see [**.scriptload (Load Script)**](-scriptload--load-script-.md)

## <span id=".SCRIPTRUN"></span>.scriptrun


The .scriptrun command will load a script, execute the root code of the script, the *initializeScript* and the *invokeScript* function. If there are any errors in the initial load and execution of the script, the errors will be displayed to console.

```
0:000> .scriptrun C:\WinDbg\Scripts\helloWorld.js
JavaScript script successfully loaded from 'C:\WinDbg\Scripts\helloWorld.js'
Hello World!  We are in JavaScript!
```

Any debugger object model manipulations made by the script will stay in place until the script is subsequently unloaded or is run again with different content.

For more information, see [**.scriptrun (Run Script)**](-scriptrun--run-script-.md).

## <span id=".scriptunload__unload_script_"></span><span id=".SCRIPTUNLOAD__UNLOAD_SCRIPT_"></span>.scriptunload (Unload Script)


The .scriptunload command unloads a loaded script and calls the *uninitializeScript* function. Use the following command syntax to unload a script

```
0:000:x86> .scriptunload C:\WinDbg\Scripts\TestScript.js
JavaScript script unloaded from 'C:\WinDbg\Scripts\TestScript.js'
```

For more information, see [**.scriptunload (Unload Script)**](-scriptunload--unload-script-.md).

## <span id=".scriptlist__list_loaded_scripts_"></span><span id=".SCRIPTLIST__LIST_LOADED_SCRIPTS_"></span>.scriptlist (List Loaded Scripts)


The .scriptlist command will list any scripts which have been loaded via the .scriptload or the .scriptrun command. If the TestScript was successfully loaded using .scriptload, the .scriptlist command would display the name of the loaded script.

```
0:000> .scriptlist
Command Loaded Scripts:
    JavaScript script from 'C:\WinDbg\Scripts\TestScript.js'
```

For more information, see [**.scriptlist (List Loaded Scripts)**](-scriptlist--list-loaded-scripts-.md).

## <span id="Started"></span><span id="started"></span><span id="STARTED"></span>Get Started with JavaScript Debugger Scripting


### <span id="HelloWorld_Example_Script"></span><span id="helloworld_example_script"></span><span id="HELLOWORLD_EXAMPLE_SCRIPT"></span>HelloWorld Example Script

This section describes how to create and execute a simple JavaScript debugger script that prints out, Hello World.

```
// WinDbg JavaScript sample
// Prints Hello World
function initializeScript()
{
    host.diagnostics.debugLog("***> Hello World! \n");
}
```

Use a text editor such as Notepad to create a text file named *HelloWorld.js* that contains the JavaScript code shown above.

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

Use the .scriptload command to load and execute the script. Because we used the function name *initializeScript*, the code in the function is run when the script is loaded.

```
0:000> .scriptload c:\WinDbg\Scripts\HelloWorld.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\HelloWorld.js'
***> Hello World! 
```

After the script is loaded the additional functionality is available in the debugger. Use the [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md) command to display *Debugger.State.Scripts* to see that our script is now resident.

```
0:000> dx Debugger.State.Scripts
Debugger.State.Scripts                
    HelloWorld 
```

In the next example, we will add and call a named function.

### <span id="Adding_Two_Values_Example_Script"></span><span id="adding_two_values_example_script"></span><span id="ADDING_TWO_VALUES_EXAMPLE_SCRIPT"></span>Adding Two Values Example Script

This section describes how to create and execute a simple JavaScript debugger script that adds takes input and adds two numbers.

This simple script provides a single function, addTwoValues.

```
// WinDbg JavaScript sample
// Adds two functions
function addTwoValues(a, b)
 {
     return a + b;
 }
```

Use a text editor such as Notepad to create a text file named *FirstSampleFunction.js*

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

Use the .scriptload command to load the script.

```
0:000> .scriptload c:\WinDbg\Scripts\FirstSampleFunction.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\FirstSampleFunction.js'
```

After the script is loaded the additional functionality is available in the debugger. Use the [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md) command to display *Debugger.State.Scripts* to see that our script is now resident.

```
0:000> dx Debugger.State.Scripts
Debugger.State.Scripts                
    FirstSampleFunction    
```

We can click on the *FirstSampleFunction*, to see what functions it provides.

```
0:000> dx -r1 -v Debugger.State.Scripts.FirstSampleFunction.Contents
Debugger.State.Scripts.FirstSampleFunction.Contents                 : [object Object]
    host             : [object Object]
    addTwoValues    
 ... 
```

To make the script a bit more convenient to work with, assign a variable in the debugger to hold the contents of the script using the dx command.

```
0:000> dx @$myScript = Debugger.State.Scripts.FirstSampleFunction.Contents
```

Use the dx expression evaluator to call the addTwoValues function.

```
0:000> dx @$myScript.addTwoValues(10, 41),d
@$myScript.addTwoValues(10, 41),d : 51
```

You can also use the *@$scriptContents* built in alias to work with the scripts. The *@$scriptContents* alias merges all of the .Content of all of the scripts that are loaded.

```
0:001> dx @$scriptContents.addTwoValues(10, 40),d
@$scriptContents.addTwoValues(10, 40),d : 50
```

When you are done working with the script use the .scriptunload command to unload the script.

```
0:000> .scriptunload c:\WinDbg\Scripts\FirstSampleFunction.js
JavaScript script successfully unloaded from 'c:\WinDbg\Scripts\FirstSampleFunction.js'
```

### <span id="Automate"></span><span id="automate"></span><span id="AUTOMATE"></span>Debugger Command Automation

This section describes how to create and execute a simple JavaScript debugger script that automates the sending of the [**u (Unassemble)**](u--unassemble-.md) command. The sample also shows how to gather and display command output in a loop.

This script provides a single function, RunCommands().

```
// WinDbg JavaScript sample
// Shows how to call a debugger command and display results
"use strict";

function RunCommands()
{
var ctl = host.namespace.Debugger.Utility.Control;   
var output = ctl.ExecuteCommand("u");
host.diagnostics.debugLog("***> Displaying command ouput \n");

for (var line of output)
   {
   host.diagnostics.debugLog("  ", line, "\n");
   }

host.diagnostics.debugLog("***> Exiting RunCommands Function \n");

}
```

Use a text editor such as Notepad to create a text file named *RunCommands.js*

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

Use the .scriptload command to load the RunCommands script.

```
0:000> .scriptload c:\WinDbg\Scripts\RunCommands.js 
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\RunCommands.js'
```

After the script is loaded the additional functionality is available in the debugger. Use the [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md) command to display *Debugger.State.Scripts.RunCommands* to see that our script is now resident.

```
0:000>dx -r3 Debugger.State.Scripts.RunCommands
Debugger.State.Scripts.RunCommands                
    Contents         : [object Object]
        host             : [object Object]
            diagnostics      : [object Object]
            namespace       
            currentSession   : Live user mode: <Local>
            currentProcess   : notepad.exe
            currentThread    : ntdll!DbgUiRemoteBreakin (00007ffd`87f2f440) 
            memory           : [object Object]
```

Use the dx command to call the RunCommands function in the RunCommands script.

```
0:000> dx Debugger.State.Scripts.RunCommands.Contents.RunCommands()
  ***> Displaying command ouput
  ntdll!ExpInterlockedPopEntrySListEnd+0x17 [d:\rs1\minkernel\ntos\rtl\amd64\slist.asm @ 196]:
  00007ffd`87f06e67 cc              int     3
  00007ffd`87f06e68 cc              int     3
  00007ffd`87f06e69 0f1f8000000000  nop     dword ptr [rax]
  ntdll!RtlpInterlockedPushEntrySList [d:\rs1\minkernel\ntos\rtl\amd64\slist.asm @ 229]:
  00007ffd`87f06e70 0f0d09          prefetchw [rcx]
  00007ffd`87f06e73 53              push    rbx
  00007ffd`87f06e74 4c8bd1          mov     r10,rcx
  00007ffd`87f06e77 488bca          mov     rcx,rdx
  00007ffd`87f06e7a 4c8bda          mov     r11,rdx
***> Exiting RunCommands Function
```

## <span id="Special_JavaScript_Debugger_Functions"></span><span id="special_javascript_debugger_functions"></span><span id="SPECIAL_JAVASCRIPT_DEBUGGER_FUNCTIONS"></span>Special JavaScript Debugger Functions


There are several special functions in a JavaScript script called by the script provider itself.

### <span id="initializeScript"></span><span id="initializescript"></span><span id="INITIALIZESCRIPT"></span>initializeScript

When a JavaScript script loads and is executed, it goes through a series of steps before the variables, functions, and other objects in the script affect the object model of the debugger.

-   The script is loaded into memory and parsed.
-   The root code in the script is executed.
-   If the script has a method called initializeScript, that method is called.
-   The return value from initializeScript is used to determine how to automatically modify the object model of the debugger.
-   The names in the script are bridged to the debugger's namespace.

As mentioned, initializeScript will be called immediately after the root code of the script is executed. Its job is to return a JavaScript array of registration objects to the provider indicating how to modify the object model of the debugger.

```
function initializeScript()
{
    // Add code here that you want to run everytime the script is loaded. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***> initializeScript was called\n");
}
```

### <span id="invokeScript"></span><span id="invokescript"></span><span id="INVOKESCRIPT"></span>invokeScript

The invokeScript method is the primary script method and is called when .scriptload and .scriptrun are run.

```
function invokeScript()
{
    // Add code here that you want to run everytime the script is executed. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***> invokeScript was called\n");
}
```

### <span id="uninitializeScript"></span><span id="uninitializescript"></span><span id="UNINITIALIZESCRIPT"></span>uninitializeScript

The uninitializeScript method is the behavioral opposite of initializeScript. It is called when a script is unlinked and is getting ready to unload. Its job is to undo any changes to the object model which the script made imperatively during execution and/or to destroy any objects which the script cached.

If a script neither makes imperative manipulations to the object model nor caches results, it does not need to have an uninitializeScript method. Any changes to the object model performed as indicated by the return value of initializeScript are undone automatically by the provider. Such changes do not require an explicit uninitializeScript method.

```
function uninitializeScript()
{
    // Add code here that you want to run everytime the script is unloaded. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***> uninitialize was called\n");
}
```

## <span id="Summary_of_Functions_Called_by_Script_Commands"></span><span id="summary_of_functions_called_by_script_commands"></span><span id="SUMMARY_OF_FUNCTIONS_CALLED_BY_SCRIPT_COMMANDS"></span>Summary of Functions Called by Script Commands


This table summarizes which functions are called by the script commands

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left">.[<strong>.scriptload</strong>](-scriptload--load-script-.md)</td>
<td align="left">[<strong>.scriptrun (Run Script)</strong>](-scriptrun--run-script-.md)</td>
<td align="left">[<strong>.scriptunload (Unload Script)</strong>](-scriptunload--unload-script-.md)</td>
</tr>
<tr class="even">
<td align="left">root</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">initializeScript</td>
<td align="left">yes</td>
<td align="left">yes</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">invokeScript</td>
<td align="left"></td>
<td align="left">yes</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">uninitializeScript</td>
<td align="left"></td>
<td align="left"></td>
<td align="left">yes</td>
</tr>
</tbody>
</table>

 

Use this sample code to see when each function is called as the script is loaded, executed and unloaded.

```
// Root of Script
host.diagnostics.debugLog("***>; Code at the very top (root) of the script is always run \n");


function initializeScript()
{
    // Add code here that you want to run everytime the script is loaded. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***>; initializeScript was called \n");
}

function invokeScript()
{
    // Add code here that you want to run everytime the script is executed. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***>; invokeScript was called \n");
}


function uninitializeScript()
{
    // Add code here that you want to run everytime the script is unloaded. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***>; uninitialize was called\n");
}


function main()
{
    // main is just another function name in JavaScript
    // main is not called by .scriptload or .scriptrun  
    host.diagnostics.debugLog("***>; main was called \n");
}
```

## <span id="Visualizer"></span><span id="visualizer"></span><span id="VISUALIZER"></span>Creating a Debugger Visualizer in JavaScript


Custom visualization files allow you to group and organize data in a visualization structure that better reflects the data relationships and content. You can use the JavaScript debugger extensions to write debugger visualizers which act in a way very similar to NatVis. This is accomplished via authoring a JavaScript prototype object (or an ES6 class) which acts as the visualizer for a given data type. For more information about NatVis and the debugger see [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md).

**Example class - Simple1DArray**

Consider an example of a C++ class which represents a single dimensional array. This class has two members, m\_size which is the overall size of the array, and m\_pValues which is a pointer to a number of ints in memory equal to the m\_size field.

```
class Simple1DArray
{
private:
 
    ULONG64 m_size;
    int *m_pValues;
};
```

We can use the dx command to look at the default data structure rendering.

```
0:000> dx g_array1D
g_array1D                 [Type: Simple1DArray]
    [+0x000] m_size           : 0x5 [Type: unsigned __int64]
    [+0x008] m_pValues        : 0x8be32449e0 : 0 [Type: int *]
```

**JavaScript Visualizer**

In order to visualize this type, we need to author a prototype (or ES6) class which has all the fields and properties we want the debugger to show. We also need to have the initializeScript method return an object which tells the JavaScript provider to link our prototype as a visualizer for the given type.

```
function initializeScript()
{
    //
    // Define a visualizer class for the object.
    //
    class myVisualizer
    {
        //
        // Create an ES6 generator function which yields back all the values in the array.
        //
        *[Symbol.iterator]()
        {
            var size = this.m_size;
            var ptr = this.m_pValues;
            for (var i = 0; i < size; ++i)
            {
                yield ptr.dereference();
 
                //
                // Note that the .add(1) method here is effectively doing pointer arithmetic on
                // the underlying pointer.  It is moving forward by the size of 1 object.
                //
                ptr = ptr.add(1);
            }
        }
    }
 
    return [new host.typeSignatureRegistration(myVisualizer, "Simple1DArray")];
}
```

Save the script in a file named arrayVisualizer.js.

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load C:\ScriptProviders\jsprovider.dll
```

Use .scriptload to load the array visualizer script.

```
0:000> .scriptload c:\WinDbg\Scripts\arrayVisualizer.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\arrayVisualizer.js'
```

Now, when the dx command is used the script visualizer will display rows of array content.

```
0:000> dx g_array1D
g_array1D                 : [object Object] [Type: Simple1DArray]
    [<Raw View>]     [Type: Simple1DArray]
    [0x0]            : 0x0
    [0x1]            : 0x1
    [0x2]            : 0x2
    [0x3]            : 0x3
    [0x4]            : 0x4
```

In addition, this JavaScript visualization provides LINQ functionality, such as Select.

```
0:000> dx g_array1D.Select(n => n * 3),d
g_array1D.Select(n => n * 3),d                
    [0]              : 0
    [1]              : 3
    [2]              : 6
    [3]              : 9
    [4]              : 12
```

**What Affects the Visualization**

A prototype or class which is made the visualizer for a native type through a return of a host.typeSignatureRegistration object from initializeScript will have all of the properties and methods within JavaScript added to the native type. In addition, the following semantics apply:

-   Any name which does not start with two underscores (\_\_) will be available in the visualization.

-   Names which are part of standard JavaScript objects or are part of protocols which the JavaScript provider creates will not show up in the visualization.

-   An object can be made iterable via the support of \[Symbol.iterator\].

-   An object can be made indexable via the support of a custom protocol consisting of several functions: getDimensionality, getValueAt, and optionally setValueAt.

**Native and JavaScript Object Bridge**

The bridge between JavaScript and the object model of the debugger is two-way. Native objects can be passed into JavaScript and JavaScript objects can be passed into the Debugger's expression evaluator. As an example of this, consider the addition of the following method in our script:

```
function multiplyBySeven(val)
{
    return val * 7;
}
```

This method can now be utilized in the example LINQ query above. First we load the JavaScript visualization.

```
0:000> .scriptload c:\WinDbg\Scripts\arrayVisualizer2.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\arrayVisualizer2.js'

0:000> dx @$myScript = Debugger.State.Scripts.arrayVisualizer2.Contents
```

Then we can use the multiplyBySeven function inline as shown below.

```
0:000> dx g_array1D.Select(@$myScript.multiplyBySeven),d
g_array1D.Select(@$myScript.multiplyBySeven),d                
    [0]              : 0
    [1]              : 7
    [2]              : 14
    [3]              : 21
    [4]              : 28
```

## <span id="Breakpoints"></span><span id="breakpoints"></span><span id="BREAKPOINTS"></span>Conditional Breakpoints with JavaScript


You can use JavaScript to do supplemental processing after a breakpoint is hit. For example, script can be used to examine other run time values and then determine if you want to automatically continue code execution or stop and do additional manual debugging.

For general information on working with breakpoints, see [Methods of Controlling Breakpoints](methods-of-controlling-breakpoints.md).

**DebugHandler.js Example Breakpoint Processing Script**

This example will evaluate notepad's open and save dialog: *notepad!ShowOpenSaveDialog*. This script will evaluate the pszCaption variable to determine if the current dialog is an "Open" dialog or if it is a "Save As" dialog. If it's an open dialog, code execution will continue. If it's a save as dialog, code execution will stop, and the debugger will break in.

```
 // Use JavaScript stric mode 
"use strict";
 
// Define the invokeScript method to handle breakpoints
 
 function invokeScript()
 {
    var ctl = host.namespace.Debugger.Utility.Control;
 
    //Get the address of my string
    var address = host.evaluateExpression("pszCaption");
 
    //The open and save dialogs use the same function
        //When we hit the open dialog, continue.
        //When we hit the save dialog, break.
    if(host.memory.readWideString(address)=="Open"){
        //host.diagnostics.debugLog("We're opening, let's continue!\n");
        ctl.ExecuteCommand("gc");
    }else{
        //host.diagnostics.debugLog("We're saving, let's break!\n");
    }
 
 }
```

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

This command sets a breakpoint on notepad!ShowOpenSaveDialog, and will run the script above whenever that breakpoint is hit.

```
bp notepad!ShowOpenSaveDialog ".scriptrun C:\\WinDbg\\Scripts\\DebugHandler.js"
```

Then when the File &gt; Save option is selected in notepad, the script is run, the g command is not sent, and a break in code execution occurs.

```
JavaScript script successfully loaded from 'C:\WinDbg\Scripts\DebugHandler.js'
notepad!ShowOpenSaveDialog:
00007ff6`f9761884 48895c2408      mov     qword ptr [rsp+8],rbx ss:000000db`d2a9f2f0=0000021985fe2060
```

## <span id="BitValues"></span><span id="bitvalues"></span><span id="BITVALUES"></span>Work With 64-Bit Values in JavaScript Extensions


This section describes how 64-bit values passed into a JavaScript debugger extension behave. This issue arises as JavaScript only has the ability to store numbers using 53-bits.

**64-Bit and JavaScript 53-Bit Storage**

Ordinal values passed into JavaScript are normally marshaled as JavaScript numbers. The problem with this is that JavaScript numbers are 64-bit double precision floating point values. Any ordinal over 53-bits would lose precision on entry into JavaScript. This presents an issue for 64-bit pointers and other 64-bit ordinal values which may have flags in the highest bytes. In order to deal with this, any 64-bit native value (whether from native code or the data model) which enters JavaScript enters as a library type -- not as a JavaScript number. This library type will round trip back to native code without losing numeric precision.

**Auto-Conversion**

The library type for 64-bit ordinal values supports the standard JavaScript valueOf conversion. If the object is used in a math operation or other construct which requires value conversion, it will automatically convert to a JavaScript number. If loss of precision were to occur (the value utilizes more than 53-bits of ordinal precision), the JavaScript provider will throw an exception.

Note that if you use bitwise operators in JavaScript, you are further limited to 32-bits of ordinal precision.

This sample code sums two numbers and will be used to test the conversion of 64 bit values.

```
function playWith64BitValues(a64, b64)
{
    // Sum two numbers to demonstrate 64-bit behavior.
    //
    // Imagine a64==100, b64==1000
    // The below would result in sum==1100 as a JavaScript number.  No exception is thrown.  The values auto-convert.
    //
    // Imagine a64==2^56, b64=1
    // The below will **Throw an Exception**.  Conversion to numeric results in loss of precision!
    //
    var sum = a64 + b64;
    host.diagnostics.debugLog("Sum   >> ", sum, "\n");
 
}

function performOp64BitValues(a64, b64, op)
{
    //
    // Call a data model method passing 64-bit value.  There is no loss of precision here.  This round trips perfectly.
    // For example:
    //  0:000> dx @$myScript.playWith64BitValues(0x4444444444444444ull, 0x3333333333333333ull, (x, y) => x + y)
    //  @$myScript.playWith64BitValues(0x4444444444444444ull, 0x3333333333333333ull, (x, y) => x + y) : 0x7777777777777777
    //
    return op(a64, b64);
}
```

Use a text editor such as Notepad to create a text file named *PlayWith64BitValues.js*

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

Use the .scriptload command to load the script.

```
0:000> .scriptload c:\WinDbg\Scripts\PlayWith64BitValues.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\PlayWith64BitValues.js'
```

To make the script a bit more convenient to work with, assign a variable in the debugger to hold the contents of the script using the dx command.

```
0:000> dx @$myScript = Debugger.State.Scripts.PlayWith64BitValues.Contents
```

Use the dx expression evaluator to call the addTwoValues function.

First we will calculate the value of 2^53 =9007199254740992 (Hex 0x20000000000000).

First to test, we will use (2^53) - 2 and see that it returns the correct value for the sum.

```
0:000> dx @$myScript.playWith64BitValues(9007199254740990, 9007199254740990)
Sum   >> 18014398509481980
```

Then we will calculate (2^53) -1 =9007199254740991. This returns the error indicating that the conversion process will lose precision, so this is the largest value that can be used with the sum method in JavaScript code.

```
0:000> dx @$myScript.playWith64BitValues(9007199254740990, 9007199254740991)
Error: 64 bit value loses precision on conversion to number
```

Call a data model method passing 64-bit values. There is no loss of precision here.

```
0:001> dx @$myScript.performOp64BitValues( 0x7FFFFFFFFFFFFFFF,  0x7FFFFFFFFFFFFFFF, (x, y) => x + y)
@$myScript.performOp64BitValues( 0x7FFFFFFFFFFFFFFF,  0x7FFFFFFFFFFFFFFF, (x, y) => x + y) : 0xfffffffffffffffe
```

**Comparison**

The 64-bit library type is a JavaScript object and not a value type such as a JavaScript number. This has some implications for comparison operations. Normally, equality (==) on an object would indicate that operands refer to the same object and not the same value. The JavaScript provider mitigates this by tracking live references to 64-bit values and returning the same "immutable" object for non-collected 64-bit value. This means that for comparison, the following would occur.

```
// Comparison with 64 Bit Values

function comparisonWith64BitValues(a64, b64)
{
    //
    // No auto-conversion occurs here.  This is an *EFFECTIVE* value comparison.  This works with ordinals with above 53-bits of precision.
    //
    var areEqual = (a64 == b64);
    host.diagnostics.debugLog("areEqual   >> ", areEqual, "\n");
    var areNotEqual = (a64 != b64);
    host.diagnostics.debugLog("areNotEqual   >> ", areNotEqual, "\n");

    //
    // Auto-conversion occurs here.  This will throw if a64 does not pack into a JavaScript number with no loss of precision.
    //
    var isEqualTo42 = (a64 == 42);
    host.diagnostics.debugLog("isEqualTo42   >> ", isEqualTo42, "\n");
    var isLess = (a64 < b64);
    host.diagnostics.debugLog("isLess   >> ", isLess, "\n");
```

Use a text editor such as Notepad to create a text file named *ComparisonWith64BitValues.js*

Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

Use the .scriptload command to load the script.

```
0:000> .scriptload c:\WinDbg\Scripts\ComparisonWith64BitValues.js
JavaScript script successfully loaded from 'c:\WinDbg\Scripts\ComparisonWith64BitValues.js'
```

To make the script a bit more convenient to work with, assign a variable in the debugger to hold the contents of the script using the dx command.

```
0:000> dx @$myScript = Debugger.State.Scripts.comparisonWith64BitValues.Contents
```

First to test, we will use (2^53) - 2 and see that it returns the expected values.

```
0:001> dx @$myScript.comparisonWith64BitValues(9007199254740990, 9007199254740990)
areEqual   >> true
areNotEqual   >> false
isEqualTo42   >> false
isLess   >> false
```

We will also try the number 42 as the first value to validate the comparison operator is working as it should.

```
0:001> dx @$myScript.comparisonWith64BitValues(42, 9007199254740990)
areEqual   >> false
areNotEqual   >> true
isEqualTo42   >> true
isLess   >> true
```

Then we will calculate (2^53) -1 =9007199254740991. This value returns the error indicating that the conversion process will lose precision, so this is the largest value that can be used with the comparison operators in JavaScript code.

```
0:000> dx @$myScript.playWith64BitValues(9007199254740990, 9007199254740991)
Error: 64 bit value loses precision on conversion to number
```

**Maintaining Precision in Operations**

In order to allow a debugger extension to maintain precision, a set of math functions are projected on top of the 64-bit library type. If the extension needs (or may possibly) need precision above 53-bits for incoming 64-bit values, the following methods should be utilized instead of relying on standard operators:

|                   |                           |                                                                                                               |
|-------------------|---------------------------|---------------------------------------------------------------------------------------------------------------|
| **Method Name**   | **Signature**             | **Description**                                                                                               |
| asNumber          | .asNumber()               | Converts the 64-bit value to a JavaScript number. If loss of precision occurs, \*\*AN EXCEPTION IS THROWN\*\* |
| convertToNumber   | .convertToNumber()        | Converts the 64-bit value to a JavaScript number. If loss of precision occurs, \*\*NO EXCEPTION IS THROWN\*\* |
| getLowPart        | .getLowPart()             | Converts the lower 32-bits of the 64-bit value to a JavaScript number                                         |
| getHighPart       | .getHighPart()            | Converts the high 32-bits of the 64-bit value to a JavaScript number                                          |
| add               | .add(value)               | Adds a value to the 64-bit value and returns the result                                                       |
| subtract          | .subtract(value)          | Subtracts a value from the 64-bit value and returns the result                                                |
| multiply          | .multiply(value)          | Multiplies the 64-bit value by the supplied value and returns the result                                      |
| divide            | .divide(value)            | Divides the 64-bit value by the supplied value and returns the result                                         |
| bitwiseAnd        | .bitwiseAnd(value)        | Computes the bitwise and of the 64-bit value with the supplied value and returns the result                   |
| bitwiseOr         | .bitwiseOr(value)         | Computes the bitwise or of the 64-bit value with the supplied value and returns the result                    |
| bitwiseXor        | .bitwiseXor(value)        | Computes the bitwise xor of the 64-bit value with the supplied value and returns the result                   |
| bitwiseShiftLeft  | .bitwiseShiftLeft(value)  | Shifts the 64-bit value left by the given amount and returns the result                                       |
| bitwiseShiftRight | .bitwiseShiftRight(value) | Shifts the 64-bit value right by the given amount and returns the result                                      |
| toString          | .toString(\[radix\])      | Converts the 64-bit value to a display string in the default radix (or the optionally supplied radix)         |

 

## <span id="Resources"></span><span id="resources"></span><span id="RESOURCES"></span>JavaScript Resources


The following are JavaScript resources that may be useful as you develop JavaScript debugging extensions.

-   [Writing JavaScript Code](https://msdn.microsoft.com/library/cte3c772.aspx)

-   [JScript Language Tour](https://msdn.microsoft.com/library/t895bwkh.aspx)

-   [Mozilla JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

-   [WinJS: The Windows library for JavaScript](https://developer.microsoft.com/windows/develop/winjs)

-   [ECMAScript 6 — New Features: Overview & Comparison](http://es6-features.org/)

## <span id="related_topics"></span>Related topics


[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20JavaScript%20Debugger%20Scripting%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





