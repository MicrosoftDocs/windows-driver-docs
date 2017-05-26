---
title: Authoring Tests in Scripting Languages
description: Authoring Tests in Scripting Languages
ms.assetid: 4F5328E4-4817-4391-BF56-EC9E7F469AA7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Authoring Tests in Scripting Languages


In addition to C++ and C#, TAEF supports authoring tests in scripting languages.

You create script components using any scripting language that supports the Microsoft COM Scripting interfaces. Script languages that support these interfaces include JScript, Microsoft Visual Basic Scripting Edition (VBScript), PERLScript, PScript, Ruby, and Python.

## <span id="Current_Limitations_of_the_Script_Test_Authoring"></span><span id="current_limitations_of_the_script_test_authoring"></span><span id="CURRENT_LIMITATIONS_OF_THE_SCRIPT_TEST_AUTHORING"></span>Current Limitations of the Script Test Authoring


Out of the box, Windows supports JScript and VBScript only.

## <span id="Script_Test_File_Format"></span><span id="script_test_file_format"></span><span id="SCRIPT_TEST_FILE_FORMAT"></span>Script Test File Format


For script language tests, TAEF uses a slightly modified [Windows Script Components](http://msdn.microsoft.com/library/07zhfkh8.aspx) file format. The following examples shows a test file that contains VBScript and JScript test classes.

```
1   <?xml version="1.0" ?>
2
3   <!-- Debugging helpers -->
4   <!-- error    Set this to true to display detailed error messages for syntax or run-time errors in the script component.-->
5   <!-- debug    Set this to true to enable debugging. If this debugging is not enabled, you cannot launch the script debugger for a script -->
6   <?component error="true" debug="true"?>
7
8   <package>
9       <!-- Test module metadata -->
10      <ModuleProperty name="Owner" value="Someone"/>
11
12      <!-- Define a test class -->
13      <component id="VBSampleTests">
14          <!-- define and instantiate a logger -->
15          <object id="Log" progid="WEX.Logger.Log" />
16  
17          <!-- include a reference to the logger so you could use the constants defined in logger library -->
18          <reference guid="e65ef678-a232-42a7-8a36-63108d719f31" version="1.0"/>
19
20          <!-- Test class metadata -->
21          <TestClassProperty name="DocumentationUrl" value="http://shelltestkb/"/>
22
23          <public>
24              <!-- Define a test method with metadata -->
25              <method name="TestOne">
26                  <!-- Test method metadata -->
27                  <TestMethodProperty name="Priority" value="1"/>
28              </method>
29  
30              <!-- Define a test method without metadata -->
31              <method name="TestTwo"/>
32         </public>
33
34          <script language="VBScript">
35              <![CDATA[
36                  Function TestOne()
37                      Log.Comment("Calling TestOne")
38                  End Function
39
40                  Function TestTwo()
41                      Log.Comment("Calling TestTwo")
42                  End Function
43              ]] >
44          </script>
45      </component>
46
47      <!-- Define another test class -->
48      <component id="JScriptSampleTests">
49          <object id="Log" progid="WEX.Logger.Log" />
50
51          <!-- need reference to use logger constants -->
52          <reference guid="e65ef678-a232-42a7-8a36-63108d719f31" version="1.0"/>
53
54          <public>
55              <!-- Test setup and cleanup methods are declared using corresponding type = &#39;&#39; attributes -->
56              <method name="ClassSetup" type="TestClassSetup"/>
57              <method name="ClassCleanup" type="TestClassCleanup"/>
58              <method name="MethodSetup"  type="TestMethodSetup"/>
59              <method name="MethodCleanup" type="TestMethodCleanup"/>
60
61              <method name="TestOne"/>
62              <method name="TestTwo"/>
63          </public>
64
65          <!-- Setup and Cleanup methods return false on failure -->
66          <script language="JScript">
67              <![CDATA[
68                  function ClassSetup()
69                  {
70                      Log.Comment("Calling class setup");
71                      return true;
72                  }
73
74                  function ClassCleanup()
75                  {
76                      Log.Comment("Calling class cleanup");
77                      return true;
78                  }
79
80                  function MethodSetup()
81                  {
82                      Log.Comment("Calling method setup");
83                      return true;
84                  }
85
86                  function MethodCleanup()
87                  {
88                      Log.Comment("Calling method cleanup");
89                      return true;
90                  }
91
92                  function TestOne()
93                  {
94                      Log.Comment("Calling TestOne");
95  
96                      // For the purpose of demonstration, declare the test failed
97                      Log.Result(TestResult_Failed);
98                  }
99
100                 function TestTwo()
101                 {
102                     Log.Comment("Calling TestTwo");
103                 }
104             ]] >
105         </script>
106     </component>
107 </package>
```

This example is an XML file and starts with an ordinary XML header:

```
<?xml version="1.0" ?>
```

You configure debug settings for your file by setting the attributes **error** and **debug**:

```
<?component error="true" debug="true"?>
```

-   Set **error** to *true* to display detailed error messages for syntax or run-time errors in the script component.
-   Set **debug** to *true* to enable debugging. If debugging is not enabled, you cannot launch the script debugger for a script (such as with the **debug** keyword within JScript code).

The **&lt;package&gt;** element encloses test class definitions in a **.wsc** file. After this element, you can insert module level metadata by adding **ModuleProperty** elements:

```
<ModuleProperty name = "Owner" value = "Someone"/>
```

The **ModuleProperty** element must include the **name** and **value** attributes.

The **Component** element starts the declaration for the script test class. This element should always have an **id** attribute that is set to the class name.

After the **Component** element, you can insert class level metadata by using the **TestClassProperty** element. As with the **ModuleProperty** element, it must have the **name** and **value** attributes.

At this point, you can also create objects and define references to the objects. See [Other Components section](http://msdn.microsoft.com/library/ye6w00x4.aspx) on MSDN for more information. Lines 15, 18, 49, and 52 in the XML example show how to reference and initialize the **WEX.Logger.Log** object.

The **&lt;public&gt;** element encloses the test script module's test method declarations. You declare a test method by specifying the test method name in the **name** attribute of a **&lt;method&gt;** element. You can also add the test method property inside the **&lt;method&gt;** element. As with properties at other levels, it is not mandatory. However, if you add it, you must include the **name** and **value** attributes.

The **&lt;script&gt;** element identifies the test script language and encloses the implementation of the test methods.

The **&lt;!\[CDATA\[\]\]&gt;** section contains the actual implementation of the tests - the code written in the scripting language. In this section, you implement the test methods that you declared in the **&lt;public&gt; &lt;/public&gt;** section.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Authoring%20Tests%20in%20Scripting%20Languages%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




