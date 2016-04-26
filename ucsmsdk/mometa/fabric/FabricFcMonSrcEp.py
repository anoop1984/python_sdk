"""This module contains the general information for FabricFcMonSrcEp ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricFcMonSrcEpConsts():
    DIRECTION_BOTH = "both"
    DIRECTION_RX = "rx"
    DIRECTION_TX = "tx"


class FabricFcMonSrcEp(ManagedObject):
    """This is FabricFcMonSrcEp class."""

    consts = FabricFcMonSrcEpConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricFcMonSrcEp", "fabricFcMonSrcEp", "mon-src-[name]", VersionMeta.Version141i, "InputOutput", 0xff, [], ["admin", "ext-san-config", "ext-san-policy"], [u'fabricFcEstcEp', u'fabricFcSanEp', u'fabricFcSanPc', u'fabricVsan', u'vmNic', u'vnicEther', u'vnicFc', u'vnicIScsi', u'vnicIScsiLCP', u'vnicIpc', u'vnicScsi'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["both", "rx", "tx"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "session": MoPropertyMeta("session", "session", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["1-255"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "direction": "direction", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "session": "session", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.direction = None
        self.sacl = None
        self.session = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricFcMonSrcEp", parent_mo_or_dn, **kwargs)
