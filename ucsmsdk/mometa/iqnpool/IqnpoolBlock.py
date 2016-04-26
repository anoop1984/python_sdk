"""This module contains the general information for IqnpoolBlock ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class IqnpoolBlockConsts():
    pass


class IqnpoolBlock(ManagedObject):
    """This is IqnpoolBlock class."""

    consts = IqnpoolBlockConsts()
    naming_props = set([u'suffix', u'from', u'to'])

    mo_meta = MoMeta("IqnpoolBlock", "iqnpoolBlock", "block-[suffix]-from-[r_from]-to-[to]", VersionMeta.Version201m, "InputOutput", 0xff, [], ["admin", "ls-storage-policy"], [u'iqnpoolPool'], [], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "ushort", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x8, None, None, None, [], ["0-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suffix": MoPropertyMeta("suffix", "suffix", "string", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x40, None, None, r"""[0-9a-zA-Z\.:-]{0,64}$""", [], []), 
        "to": MoPropertyMeta("to", "to", "ushort", VersionMeta.Version201m, MoPropertyMeta.NAMING, 0x80, None, None, None, [], ["0-65535"]), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "from": "r_from", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suffix": "suffix", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, suffix, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.suffix = suffix
        self.r_from = r_from
        self.to = to
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "IqnpoolBlock", parent_mo_or_dn, **kwargs)
