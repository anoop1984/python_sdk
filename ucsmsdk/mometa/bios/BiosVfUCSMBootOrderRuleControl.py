"""This module contains the general information for BiosVfUCSMBootOrderRuleControl ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class BiosVfUCSMBootOrderRuleControlConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_UCSMBOOT_ORDER_RULE_LOOSE = "loose"
    VP_UCSMBOOT_ORDER_RULE_PLATFORM_DEFAULT = "platform-default"
    VP_UCSMBOOT_ORDER_RULE_PLATFORM_RECOMMENDED = "platform-recommended"
    VP_UCSMBOOT_ORDER_RULE_STRICT = "strict"


class BiosVfUCSMBootOrderRuleControl(ManagedObject):
    """This is BiosVfUCSMBootOrderRuleControl class."""

    consts = BiosVfUCSMBootOrderRuleControlConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfUCSMBootOrderRuleControl", "biosVfUCSMBootOrderRuleControl", "UCSM-Boot-Order-Rule-Control", VersionMeta.Version142b, "InputOutput", 0x1f, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version142b, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_ucsm_boot_order_rule": MoPropertyMeta("vp_ucsm_boot_order_rule", "vpUCSMBootOrderRule", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["loose", "platform-default", "platform-recommended", "strict"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpUCSMBootOrderRule": "vp_ucsm_boot_order_rule", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_ucsm_boot_order_rule = None

        ManagedObject.__init__(self, "BiosVfUCSMBootOrderRuleControl", parent_mo_or_dn, **kwargs)

