---
ms.assetid: 8BADC31C-6446-41FA-82F3-F46D66954481
title: How to add test metadata
description: Create test content for Windows 8, using the Windows Driver Kit (WDK) and the Test Authoring and Execution Framework (TAEF).
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to add test metadata

For Windows 8, the Windows Driver Kit (WDK) uses the [Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439725) for creating test content. A TAEF test is an object implemented as a dynamic-link library (DLL) that contains multiple methods, where each method maps to a specific test scenario. The TAEF object combines related methods into a group of tests. For each test, there is a set of metadata that describes the test. To improve test portability and encapsulation, TAEF stores test metadata within the test object itself. When you create your own driver tests using the Driver Test templates, you need to add this metadata so that your driver tests are available and can be deployed using Visual Studio.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   The source code for a driver test written by using one of the Driver Test templates. For information, see [How to write a driver test using a Driver Test template](how-to-write-a-driver-test-.md).

### <span id="To_add_test_metadata_attributes"></span><span id="to_add_test_metadata_attributes"></span><span id="TO_ADD_TEST_METADATA_ATTRIBUTES"></span>To add test metadata attributes

1.  Add the required test property metadata to the source files for your test.
2.  For example, if you use the Driver Test template to create your version of the SurpriseRemove test, the following metadata is added. Edit the test description, display name, category, and results file attributes.

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>// Declare the test class method DoSurpriseRemove - the main test method within this class
        BEGIN_TEST_METHOD(DoSurpriseRemove)
        // Required properties for driver tests
        TEST_METHOD_PROPERTY(L&quot;Kits.Drivers&quot;, L&quot;TRUE&quot;)
        TEST_METHOD_PROPERTY(L&quot;Kits.Parameter&quot;, L&quot;DQ&quot;)
        TEST_METHOD_PROPERTY(L&quot;Kits.Parameter.DQ.Description&quot;, L&quot;A WDTF SDEL query that is used to identify the target device(s) - http://go.microsoft.com/fwlink/p/?linkid=232678&quot;)
        TEST_METHOD_PROPERTY(L&quot;Kits.Parameter.DQ.Default&quot;, L&quot;INF::OriginalInfFileName=&#39;%InfFileName%&#39;&quot;)  
        TEST_METHOD_PROPERTY(L&quot;RebootPossible&quot;, L&quot;true&quot;)
        // TODO: Required properties to be customized to match your test requirements
        TEST_METHOD_PROPERTY(L&quot;Description&quot;, L&quot;Plug and Play Surprise Remove Generated Template&quot;)
        TEST_METHOD_PROPERTY(L&quot;Kits.DisplayName&quot;, L&quot;My Plug and Play Surprise Remove Test&quot;) 
        TEST_METHOD_PROPERTY(L&quot;Kits.Category&quot;, L&quot;My Test Category&quot;)
        // Optional properties for driver tests
        TEST_METHOD_PROPERTY(L&quot;Kits.Drivers.ResultFile&quot;, L&quot;TestTextLog.log&quot;)
        // TODO: (see Windows Driver Kit documentation for additional optional properties)
        END_TEST_METHOD()</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="CSharp"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C#</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>//
        // DoSurpriseRemove is a test method as identified by the [TestMethod] tag. 
        // More methods can be added by following this basic pattern.
        // The name of the function defines the name of the test.
        //
        [TestMethod]
        // Required properties (see Windows Driver Kit documentation for more information):
        [TestProperty(&quot;Kits.Drivers&quot;, &quot;TRUE&quot;)]
        [TestProperty(&quot;Kits.Parameter&quot;, &quot;DQ&quot;)]
        [TestProperty(&quot;Kits.Parameter.DQ.Description&quot;, &quot;A WDTF SDEL query that is used to identify the target device(s) - http://go.microsoft.com/fwlink/p/?linkid=232678&quot;)]
        [TestProperty(&quot;Kits.Parameter.DQ.Default&quot;, &quot;INF::OriginalInfFileName=&#39;%InfFileName%&#39;&quot;)]
        // TODO: Required properties to be customized to match your test requirements.
        [TestProperty(&quot;Description&quot;, &quot;Plug and Play Surprise Remove Generated Template&quot;)]
        [TestProperty(&quot;Kits.DisplayName&quot;, &quot;My Plug and Play Surprise Remove Test&quot;)]
        [TestProperty(&quot;Kits.Category&quot;, &quot;My Test Category&quot;)]
        [TestProperty(&quot;RebootPossible&quot;, &quot;true&quot;)]
        // Optional properties (see Windows Driver Kit documentation for additional optional properties):
        [TestProperty(&quot;Kits.Drivers.ResultFile&quot;, &quot;TestTextLog.log&quot;)]</code></pre></td>
    </tr>
    </tbody>
    </table>

    Windows Script Component (.wsc)

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>&lt;!-- Define a test method with metadata: --&gt;
        &lt;method name=&quot;PlugAndPlaySurpriseRemoveTest&quot;&gt;
        &lt;!-- Required properties for ERT--&gt;
        &lt;TestMethodProperty name=&quot;Kits.Drivers&quot; value=&quot;TRUE&quot;/&gt;
        &lt;TestMethodProperty name=&quot;Kits.Parameter&quot; value=&quot;DQ&quot;/&gt;
        &lt;TestMethodProperty name=&quot;Kits.Parameter.DQ.Description&quot; value=&quot;A WDTF SDEL query that is used to identify the target device(s) - http://go.microsoft.com/fwlink/p/?linkid=232678&quot;/&gt;
        &lt;TestMethodProperty name=&quot;Kits.Parameter.DQ.Default&quot; value=&quot;INF::OriginalInfFileName=&#39;%InfFileName%&#39;&quot;/&gt;
        &lt;TestMethodProperty name=&quot;RebootPossible&quot; value=&quot;true&quot; /&gt;
        &lt;!-- TODO: Properties to be customized to match your test requirements --&gt;
        &lt;TestMethodProperty name=&quot;Description&quot; value=&quot;Plug and Play Surprise Remove Generated Template&quot;/&gt;
        &lt;TestMethodProperty name=&quot;Kits.DisplayName&quot; value=&quot;My Plug and Play Surprise Remove Test&quot;/&gt;
        &lt;TestMethodProperty name=&quot;Kits.Category&quot; value=&quot;My Test Category&quot;/&gt;
        &lt;!-- Optional properties for ERT--&gt;
        &lt;TestMethodProperty name=&quot;Kits.Drivers.ResultFile&quot; value=&quot;TestTextLog.log&quot;/&gt;
        &lt;!-- (see Windows Driver Kit documentation for additional optional properties) --&gt;
        &lt;/method&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

3.  The following table describes the test property attributes. Use the examples for guidance as you edit or add the metadata for your tests.

    <span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**  
    A short description of what the test does.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 
      &lt; TestProperty name=&quot;Description&quot; value= &quot;This test cycles the system through various sleep states and performs IO on devices before and after each sleep state cycle&quot;/&gt;
    </code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[C++]
      
     TEST_METHOD_PROPERTY(L&quot;Description&quot;, L&quot;Plug and Play Surprise Remove Generated Template&quot;)</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>**DisplayName**  
    The name of the test as it shown in Driver Test.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 
      
     &lt; TestProperty name=&quot;Kits.DisplayName&quot; value=&quot;Sleep with IO Before and After&quot;/&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code> [C++]

      TEST_METHOD_PROPERTY(L&quot;Kits.DisplayName&quot;, L&quot;My Plug and Play Surprise Remove Test&quot;) </code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Kits.Parameter"></span><span id="kits.parameter"></span><span id="KITS.PARAMETER"></span>**Kits.Parameter**  
    A standard parameter for a method call. A test can have multiple parameters.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 

    &lt;ModuleProperty name=&quot;Kits.Parameter&quot; value=&quot;TM&quot;/&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[C++]

    TEST_METHOD_PROPERTY(L&quot;Kits.Parameter&quot;, L&quot;DQ&quot;)</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Kits.Parameter._ParameterName_.Description"></span><span id="kits.parameter._parametername_.description"></span><span id="KITS.PARAMETER._PARAMETERNAME_.DESCRIPTION"></span>**Kits.Parameter.***&lt;ParameterName&gt;***.Description**  
    The description for the parameter.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 
      
    &lt; TestProperty name=&quot;Kits.Parameter.TM.Description&quot; value=&quot;Test mode parameter: Logo or Simple&quot;/&gt; </code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code> 
    [C++]

    TEST_METHOD_PROPERTY(L&quot;Kits.Parameter.DQ.Description&quot;, L&quot;A WDTF SDEL query that is used to identify the target device(s)&quot;)</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Kits.Parameter._ParameterName_.Default"></span><span id="kits.parameter._parametername_.default"></span><span id="KITS.PARAMETER._PARAMETERNAME_.DEFAULT"></span>**Kits.Parameter.***&lt;ParameterName&gt;***.Default**  
    The default value for the parameter.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 

    &lt; TestProperty name=&quot;Kits.Parameter.TM.Default&quot; value=&quot;Logo&quot;/&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[C++]

     TEST_METHOD_PROPERTY(L&quot;Kits.Parameter.DQ.Default&quot;, L&quot;INF::OriginalInfFileName=&#39;%InfFileName%&#39;&quot;)  </code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Kits.Drivers"></span><span id="kits.drivers"></span><span id="KITS.DRIVERS"></span>**Kits.Drivers**  
    This attribute marks the test for inclusion in the WDK.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[Script] 
      
    &lt; TestProperty name=&quot;Kits.Drivers&quot; value=&quot;&quot;/&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[C++]

     TEST_METHOD_PROPERTY(L&quot;Kits.Drivers&quot;, L&quot;TRUE&quot;)</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Kits.Category"></span><span id="kits.category"></span><span id="KITS.CATEGORY"></span>**Kits.Category**  
    Describes the category of a test.

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code> [Script] 
      
    &lt; TestProperty name=&quot;Kits.Category&quot; value=&quot;Logo\Device Fundamentals&quot;/&gt;</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code> [C++]

    TEST_METHOD_PROPERTY(L&quot;Kits.Category&quot;, L&quot;My Test Category&quot;)</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span id="Deploymentitem"></span><span id="deploymentitem"></span><span id="DEPLOYMENTITEM"></span>**Deploymentitem**  
    Identifies files and/or folders as test dependencies. These may contain any resources needed to run the tests. For more information about using this metadata, see [DeploymentItem Metadata](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439604).

## <span id="related_topics"></span>Related topics


* [How to write a driver test using a Driver Test template](how-to-write-a-driver-test-.md)
 

 






