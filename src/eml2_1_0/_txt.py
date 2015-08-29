# ./_txt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a5526fb15776f6f23169a92b77bd98e9a242b685
# Generated 2015-08-28 15:11:58.471747 by PyXB version 1.2.3
# Namespace eml://ecoinformatics.org/text-2.1.0 [xmlns:txt]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6a2e302a-4dc9-11e5-a116-000c2950e125')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'eml://ecoinformatics.org/text-2.1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {eml://ecoinformatics.org/text-2.1.0}TextType with content type MIXED
class TextType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TextType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element section uses Python identifier section
    __section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'section'), 'section', '__emlecoinformatics_orgtext_2_1_0_TextType_section', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 102, 6), )

    
    section = property(__section.value, __section.set, None, u'')

    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'para'), 'para', '__emlecoinformatics_orgtext_2_1_0_TextType_para', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 115, 6), )

    
    para = property(__para.value, __para.set, None, u'')

    _ElementMap.update({
        __section.name() : __section,
        __para.name() : __para
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TextType', TextType)


# Complex type {eml://ecoinformatics.org/text-2.1.0}ParagraphType with content type MIXED
class ParagraphType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParagraphType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 132, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element itemizedlist uses Python identifier itemizedlist
    __itemizedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'itemizedlist'), 'itemizedlist', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_itemizedlist', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 147, 6), )

    
    itemizedlist = property(__itemizedlist.value, __itemizedlist.set, None, u'')

    
    # Element orderedlist uses Python identifier orderedlist
    __orderedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'orderedlist'), 'orderedlist', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_orderedlist', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 161, 6), )

    
    orderedlist = property(__orderedlist.value, __orderedlist.set, None, u'')

    
    # Element emphasis uses Python identifier emphasis
    __emphasis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'emphasis'), 'emphasis', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_emphasis', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 175, 6), )

    
    emphasis = property(__emphasis.value, __emphasis.set, None, u'')

    
    # Element subscript uses Python identifier subscript
    __subscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'subscript'), 'subscript', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_subscript', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 188, 6), )

    
    subscript = property(__subscript.value, __subscript.set, None, u'')

    
    # Element superscript uses Python identifier superscript
    __superscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'superscript'), 'superscript', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_superscript', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 199, 6), )

    
    superscript = property(__superscript.value, __superscript.set, None, u'')

    
    # Element literalLayout uses Python identifier literalLayout
    __literalLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'literalLayout'), 'literalLayout', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_literalLayout', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 210, 6), )

    
    literalLayout = property(__literalLayout.value, __literalLayout.set, None, u'')

    
    # Element ulink uses Python identifier ulink
    __ulink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ulink'), 'ulink', '__emlecoinformatics_orgtext_2_1_0_ParagraphType_ulink', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 226, 6), )

    
    ulink = property(__ulink.value, __ulink.set, None, u'')

    _ElementMap.update({
        __itemizedlist.name() : __itemizedlist,
        __orderedlist.name() : __orderedlist,
        __emphasis.name() : __emphasis,
        __subscript.name() : __subscript,
        __superscript.name() : __superscript,
        __literalLayout.name() : __literalLayout,
        __ulink.name() : __ulink
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ParagraphType', ParagraphType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 235, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element citetitle uses Python identifier citetitle
    __citetitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citetitle'), 'citetitle', '__emlecoinformatics_orgtext_2_1_0_CTD_ANON_citetitle', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 237, 12), )

    
    citetitle = property(__citetitle.value, __citetitle.set, None, u'')

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'url'), 'url', '__emlecoinformatics_orgtext_2_1_0_CTD_ANON_url', pyxb.binding.datatypes.anySimpleType)
    __url._DeclarationLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 248, 10)
    __url._UseLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 248, 10)
    
    url = property(__url.value, __url.set, None, u'')

    _ElementMap.update({
        __citetitle.name() : __citetitle
    })
    _AttributeMap.update({
        __url.name() : __url
    })



# Complex type {eml://ecoinformatics.org/text-2.1.0}SectionType with content type ELEMENT_ONLY
class SectionType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SectionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 271, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__emlecoinformatics_orgtext_2_1_0_SectionType_title', False, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 284, 6), )

    
    title = property(__title.value, __title.set, None, u'')

    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'para'), 'para', '__emlecoinformatics_orgtext_2_1_0_SectionType_para', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 297, 8), )

    
    para = property(__para.value, __para.set, None, u'')

    
    # Element section uses Python identifier section
    __section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'section'), 'section', '__emlecoinformatics_orgtext_2_1_0_SectionType_section', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 312, 8), )

    
    section = property(__section.value, __section.set, None, u'')

    _ElementMap.update({
        __title.name() : __title,
        __para.name() : __para,
        __section.name() : __section
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SectionType', SectionType)


# Complex type {eml://ecoinformatics.org/text-2.1.0}ListType with content type ELEMENT_ONLY
class ListType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ListType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 328, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element listitem uses Python identifier listitem
    __listitem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'listitem'), 'listitem', '__emlecoinformatics_orgtext_2_1_0_ListType_listitem', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 341, 8), )

    
    listitem = property(__listitem.value, __listitem.set, None, u'')

    _ElementMap.update({
        __listitem.name() : __listitem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ListType', ListType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 355, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'para'), 'para', '__emlecoinformatics_orgtext_2_1_0_CTD_ANON__para', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 357, 14), )

    
    para = property(__para.value, __para.set, None, u'')

    
    # Element itemizedlist uses Python identifier itemizedlist
    __itemizedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'itemizedlist'), 'itemizedlist', '__emlecoinformatics_orgtext_2_1_0_CTD_ANON__itemizedlist', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 372, 14), )

    
    itemizedlist = property(__itemizedlist.value, __itemizedlist.set, None, u'')

    
    # Element orderedlist uses Python identifier orderedlist
    __orderedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'orderedlist'), 'orderedlist', '__emlecoinformatics_orgtext_2_1_0_CTD_ANON__orderedlist', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 386, 14), )

    
    orderedlist = property(__orderedlist.value, __orderedlist.set, None, u'')

    _ElementMap.update({
        __para.name() : __para,
        __itemizedlist.name() : __itemizedlist,
        __orderedlist.name() : __orderedlist
    })
    _AttributeMap.update({
        
    })



# Complex type {eml://ecoinformatics.org/text-2.1.0}SubSuperScriptType with content type MIXED
class SubSuperScriptType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SubSuperScriptType')
    _XSDLocation = pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 405, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element subscript uses Python identifier subscript
    __subscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'subscript'), 'subscript', '__emlecoinformatics_orgtext_2_1_0_SubSuperScriptType_subscript', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 419, 6), )

    
    subscript = property(__subscript.value, __subscript.set, None, u'')

    
    # Element superscript uses Python identifier superscript
    __superscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'superscript'), 'superscript', '__emlecoinformatics_orgtext_2_1_0_SubSuperScriptType_superscript', True, pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 430, 6), )

    
    superscript = property(__superscript.value, __superscript.set, None, u'')

    _ElementMap.update({
        __subscript.name() : __subscript,
        __superscript.name() : __superscript
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SubSuperScriptType', SubSuperScriptType)


text = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'text'), TextType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 74, 2))
Namespace.addCategoryObject('elementBinding', text.name().localName(), text)



TextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'section'), SectionType, scope=TextType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 102, 6)))

TextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'para'), ParagraphType, scope=TextType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 115, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 102, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 115, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TextType._UseForTag(pyxb.namespace.ExpandedName(None, u'section')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 102, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TextType._UseForTag(pyxb.namespace.ExpandedName(None, u'para')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 115, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TextType._Automaton = _BuildAutomaton()




ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'itemizedlist'), ListType, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 147, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'orderedlist'), ListType, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 161, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'emphasis'), pyxb.binding.datatypes.string, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 175, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'subscript'), SubSuperScriptType, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 188, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'superscript'), SubSuperScriptType, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 199, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'literalLayout'), pyxb.binding.datatypes.string, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 210, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ulink'), CTD_ANON, scope=ParagraphType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 226, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 146, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 226, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'itemizedlist')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 147, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'orderedlist')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 161, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'emphasis')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 175, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'subscript')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 188, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'superscript')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 199, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'literalLayout')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 210, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, u'ulink')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 226, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ParagraphType._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citetitle'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 237, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 236, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'citetitle')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 237, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()




SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=SectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 284, 6)))

SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'para'), ParagraphType, scope=SectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 297, 8)))

SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'section'), SectionType, scope=SectionType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 312, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 284, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 284, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'para')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 297, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, u'section')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 312, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SectionType._Automaton = _BuildAutomaton_3()




ListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'listitem'), CTD_ANON_, scope=ListType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 341, 8)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ListType._UseForTag(pyxb.namespace.ExpandedName(None, u'listitem')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 341, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ListType._Automaton = _BuildAutomaton_4()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'para'), ParagraphType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 357, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'itemizedlist'), ListType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 372, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'orderedlist'), ListType, scope=CTD_ANON_, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 386, 14)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'para')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 357, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'itemizedlist')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 372, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'orderedlist')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 386, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_5()




SubSuperScriptType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'subscript'), SubSuperScriptType, scope=SubSuperScriptType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 419, 6)))

SubSuperScriptType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'superscript'), SubSuperScriptType, scope=SubSuperScriptType, documentation=u'', location=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 430, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 418, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubSuperScriptType._UseForTag(pyxb.namespace.ExpandedName(None, u'subscript')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 419, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubSuperScriptType._UseForTag(pyxb.namespace.ExpandedName(None, u'superscript')), pyxb.utils.utility.Location(u'/home/servilla/local/lib/eml-2.1.0/eml-text.xsd', 430, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubSuperScriptType._Automaton = _BuildAutomaton_6()

