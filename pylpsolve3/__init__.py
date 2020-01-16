import lpsolve55

# BEGIN CONSTANTS
ANTIDEGEN_BOUNDFLIP = lpsolve55.ANTIDEGEN_BOUNDFLIP
ANTIDEGEN_COLUMNCHECK = lpsolve55.ANTIDEGEN_COLUMNCHECK
ANTIDEGEN_DURINGBB = lpsolve55.ANTIDEGEN_DURINGBB
ANTIDEGEN_DYNAMIC = lpsolve55.ANTIDEGEN_DYNAMIC
ANTIDEGEN_FIXEDVARS = lpsolve55.ANTIDEGEN_FIXEDVARS
ANTIDEGEN_INFEASIBLE = lpsolve55.ANTIDEGEN_INFEASIBLE
ANTIDEGEN_LOSTFEAS = lpsolve55.ANTIDEGEN_LOSTFEAS
ANTIDEGEN_NONE = lpsolve55.ANTIDEGEN_NONE
ANTIDEGEN_NUMFAILURE = lpsolve55.ANTIDEGEN_NUMFAILURE
ANTIDEGEN_RHSPERTURB = lpsolve55.ANTIDEGEN_RHSPERTURB
ANTIDEGEN_STALLING = lpsolve55.ANTIDEGEN_STALLING
BRANCH_AUTOMATIC = lpsolve55.BRANCH_AUTOMATIC
BRANCH_DEFAULT = lpsolve55.BRANCH_DEFAULT
BRANCH_CEILING = lpsolve55.BRANCH_CEILING
BRANCH_FLOOR = lpsolve55.BRANCH_FLOOR
CRASH_LEASTDEGENERATE = lpsolve55.CRASH_LEASTDEGENERATE
CRASH_MOSTFEASIBLE = lpsolve55.CRASH_MOSTFEASIBLE
CRASH_NONE = lpsolve55.CRASH_NONE
CRITICAL = lpsolve55.CRITICAL
DEGENERATE = lpsolve55.DEGENERATE
DETAILED = lpsolve55.DETAILED
EQ = lpsolve55.EQ
FEASFOUND = lpsolve55.FEASFOUND
FR = lpsolve55.FR
FULL = lpsolve55.FULL
GE = lpsolve55.GE
IMPORTANT = lpsolve55.IMPORTANT
IMPROVE_BBSIMPLEX = lpsolve55.IMPROVE_BBSIMPLEX
IMPROVE_DUALFEAS = lpsolve55.IMPROVE_DUALFEAS
IMPROVE_NONE = lpsolve55.IMPROVE_NONE
IMPROVE_SOLUTION = lpsolve55.IMPROVE_SOLUTION
IMPROVE_THETAGAP = lpsolve55.IMPROVE_THETAGAP
INFEASIBLE = lpsolve55.INFEASIBLE
Infinite = lpsolve55.Infinite
LE = lpsolve55.LE
MSG_LPFEASIBLE = lpsolve55.MSG_LPFEASIBLE
MSG_LPOPTIMAL = lpsolve55.MSG_LPOPTIMAL
MSG_MILPBETTER = lpsolve55.MSG_MILPBETTER
MSG_MILPEQUAL = lpsolve55.MSG_MILPEQUAL
MSG_MILPFEASIBLE = lpsolve55.MSG_MILPFEASIBLE
MSG_PRESOLVE = lpsolve55.MSG_PRESOLVE
NEUTRAL = lpsolve55.NEUTRAL
NODE_AUTOORDER = lpsolve55.NODE_AUTOORDER
NODE_BRANCHREVERSEMODE = lpsolve55.NODE_BRANCHREVERSEMODE
NODE_BREADTHFIRSTMODE = lpsolve55.NODE_BREADTHFIRSTMODE
NODE_DEPTHFIRSTMODE = lpsolve55.NODE_DEPTHFIRSTMODE
NODE_DYNAMICMODE = lpsolve55.NODE_DYNAMICMODE
NODE_FIRSTSELECT = lpsolve55.NODE_FIRSTSELECT
NODE_FRACTIONSELECT = lpsolve55.NODE_FRACTIONSELECT
NODE_GAPSELECT = lpsolve55.NODE_GAPSELECT
NODE_GREEDYMODE = lpsolve55.NODE_GREEDYMODE
NODE_GUBMODE = lpsolve55.NODE_GUBMODE
NODE_PSEUDOCOSTMODE = lpsolve55.NODE_PSEUDOCOSTMODE
NODE_PSEUDOCOSTSELECT = lpsolve55.NODE_PSEUDOCOSTSELECT
NODE_PSEUDONONINTSELECT = lpsolve55.NODE_PSEUDONONINTSELECT
NODE_PSEUDORATIOSELECT = lpsolve55.NODE_PSEUDORATIOSELECT
NODE_RANDOMIZEMODE = lpsolve55.NODE_RANDOMIZEMODE
NODE_RANGESELECT = lpsolve55.NODE_RANGESELECT
NODE_RCOSTFIXING = lpsolve55.NODE_RCOSTFIXING
NODE_RESTARTMODE = lpsolve55.NODE_RESTARTMODE
NODE_STRONGINIT = lpsolve55.NODE_STRONGINIT
NODE_USERSELECT = lpsolve55.NODE_USERSELECT
NODE_WEIGHTREVERSEMODE = lpsolve55.NODE_WEIGHTREVERSEMODE
NOFEASFOUND = lpsolve55.NOFEASFOUND
NOMEMORY = lpsolve55.NOMEMORY
NORMAL = lpsolve55.NORMAL
NUMFAILURE = lpsolve55.NUMFAILURE
OPTIMAL = lpsolve55.OPTIMAL
PRESOLVED = lpsolve55.PRESOLVED
PRESOLVE_BOUNDS = lpsolve55.PRESOLVE_BOUNDS
PRESOLVE_COLDOMINATE = lpsolve55.PRESOLVE_COLDOMINATE
PRESOLVE_COLFIXDUAL = lpsolve55.PRESOLVE_COLFIXDUAL
PRESOLVE_COLS = lpsolve55.PRESOLVE_COLS
PRESOLVE_DUALS = lpsolve55.PRESOLVE_DUALS
PRESOLVE_ELIMEQ2 = lpsolve55.PRESOLVE_ELIMEQ2
PRESOLVE_IMPLIEDFREE = lpsolve55.PRESOLVE_IMPLIEDFREE
PRESOLVE_IMPLIEDSLK = lpsolve55.PRESOLVE_IMPLIEDSLK
PRESOLVE_KNAPSACK = lpsolve55.PRESOLVE_KNAPSACK
PRESOLVE_LINDEP = lpsolve55.PRESOLVE_LINDEP
PRESOLVE_MERGEROWS = lpsolve55.PRESOLVE_MERGEROWS
PRESOLVE_NONE = lpsolve55.PRESOLVE_NONE
PRESOLVE_PROBEFIX = lpsolve55.PRESOLVE_PROBEFIX
PRESOLVE_PROBEREDUCE = lpsolve55.PRESOLVE_PROBEREDUCE
PRESOLVE_REDUCEGCD = lpsolve55.PRESOLVE_REDUCEGCD
PRESOLVE_REDUCEMIP = lpsolve55.PRESOLVE_REDUCEMIP
PRESOLVE_ROWDOMINATE = lpsolve55.PRESOLVE_ROWDOMINATE
PRESOLVE_ROWS = lpsolve55.PRESOLVE_ROWS
PRESOLVE_SENSDUALS = lpsolve55.PRESOLVE_SENSDUALS
PRESOLVE_SOS = lpsolve55.PRESOLVE_SOS
PRICER_DANTZIG = lpsolve55.PRICER_DANTZIG
PRICER_DEVEX = lpsolve55.PRICER_DEVEX
PRICER_FIRSTINDEX = lpsolve55.PRICER_FIRSTINDEX
PRICER_STEEPESTEDGE = lpsolve55.PRICER_STEEPESTEDGE
PRICE_ADAPTIVE = lpsolve55.PRICE_ADAPTIVE
PRICE_AUTOPARTIAL = lpsolve55.PRICE_AUTOPARTIAL
PRICE_HARRISTWOPASS = lpsolve55.PRICE_HARRISTWOPASS
PRICE_LOOPALTERNATE = lpsolve55.PRICE_LOOPALTERNATE
PRICE_LOOPLEFT = lpsolve55.PRICE_LOOPLEFT
PRICE_MULTIPLE = lpsolve55.PRICE_MULTIPLE
PRICE_PARTIAL = lpsolve55.PRICE_PARTIAL
PRICE_PRIMALFALLBACK = lpsolve55.PRICE_PRIMALFALLBACK
PRICE_RANDOMIZE = lpsolve55.PRICE_RANDOMIZE
PRICE_TRUENORMINIT = lpsolve55.PRICE_TRUENORMINIT
PROCBREAK = lpsolve55.PROCBREAK
PROCFAIL = lpsolve55.PROCFAIL
SCALE_COLSONLY = lpsolve55.SCALE_COLSONLY
SCALE_CURTISREID = lpsolve55.SCALE_CURTISREID
SCALE_DYNUPDATE = lpsolve55.SCALE_DYNUPDATE
SCALE_EQUILIBRATE = lpsolve55.SCALE_EQUILIBRATE
SCALE_EXTREME = lpsolve55.SCALE_EXTREME
SCALE_GEOMETRIC = lpsolve55.SCALE_GEOMETRIC
SCALE_INTEGERS = lpsolve55.SCALE_INTEGERS
SCALE_LOGARITHMIC = lpsolve55.SCALE_LOGARITHMIC
SCALE_MEAN = lpsolve55.SCALE_MEAN
SCALE_NONE = lpsolve55.SCALE_NONE
SCALE_POWER2 = lpsolve55.SCALE_POWER2
SCALE_QUADRATIC = lpsolve55.SCALE_QUADRATIC
SCALE_RANGE = lpsolve55.SCALE_RANGE
SCALE_ROWSONLY = lpsolve55.SCALE_ROWSONLY
SCALE_USERWEIGHT = lpsolve55.SCALE_USERWEIGHT
SEVERE = lpsolve55.SEVERE
SIMPLEX_DUAL_DUAL = lpsolve55.SIMPLEX_DUAL_DUAL
SIMPLEX_DUAL_PRIMAL = lpsolve55.SIMPLEX_DUAL_PRIMAL
SIMPLEX_PRIMAL_DUAL = lpsolve55.SIMPLEX_PRIMAL_DUAL
SIMPLEX_PRIMAL_PRIMAL = lpsolve55.SIMPLEX_PRIMAL_PRIMAL
SUBOPTIMAL = lpsolve55.SUBOPTIMAL
TIMEOUT = lpsolve55.TIMEOUT
UNBOUNDED = lpsolve55.UNBOUNDED
USERABORT = lpsolve55.USERABORT
# END CONSTANTS

# BEGIN FUNCTIONS
# This function was generated programtically, please do not modify
def add_column(*args, decode_return=False):
    """return = lpsolve('add_column', lp, [column])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'add_column', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'add_column', *encode_args(args))


# This function was generated programtically, please do not modify
def add_columnex(*args, decode_return=False):
    """return = lpsolve('add_columnex', lp, [column])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'add_columnex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'add_columnex', *encode_args(args))


# This function was generated programtically, please do not modify
def add_constraint(*args, decode_return=False):
    """return = lpsolve('add_constraint', lp, [row], constr_type, rh)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'add_constraint', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'add_constraint', *encode_args(args))


# This function was generated programtically, please do not modify
def add_constraintex(*args, decode_return=False):
    """return = lpsolve('add_constraintex', lp, [row], constr_type, rh)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'add_constraintex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'add_constraintex', *encode_args(args))


# This function was generated programtically, please do not modify
def add_SOS(*args, decode_return=False):
    """return = lpsolve('add_SOS', lp, name, sostype, priority, [sosvars], [weights])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'add_SOS', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'add_SOS', *encode_args(args))


# This function was generated programtically, please do not modify
def column_in_lp(*args, decode_return=False):
    """return = lpsolve('column_in_lp', lp, [column])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'column_in_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'column_in_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def copy_lp(*args, decode_return=False):
    """lp_handle = lpsolve('copy_lp', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'copy_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'copy_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def default_basis(*args, decode_return=False):
    """lpsolve('default_basis', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'default_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'default_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def del_column(*args, decode_return=False):
    """return = lpsolve('del_column', lp, column)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'del_column', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'del_column', *encode_args(args))


# This function was generated programtically, please do not modify
def del_constraint(*args, decode_return=False):
    """return = lpsolve('del_constraint', lp, del_row)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'del_constraint', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'del_constraint', *encode_args(args))


# This function was generated programtically, please do not modify
def delete_lp(*args, decode_return=False):
    """lpsolve('delete_lp', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'delete_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'delete_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def free_lp(*args, decode_return=False):
    """lpsolve('free_lp', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'free_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'free_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def get_anti_degen(*args, decode_return=False):
    """return = lpsolve('get_anti_degen', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_anti_degen', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_anti_degen', *encode_args(args))


# This function was generated programtically, please do not modify
def get_basis(*args, decode_return=False):
    """[bascolumn] = lpsolve('get_basis', lp {, nonbasic})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def get_basiscrash(*args, decode_return=False):
    """return = lpsolve('get_basiscrash', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_basiscrash', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_basiscrash', *encode_args(args))


# This function was generated programtically, please do not modify
def get_bb_depthlimit(*args, decode_return=False):
    """return = lpsolve('get_bb_depthlimit', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_bb_depthlimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_bb_depthlimit', *encode_args(args))


# This function was generated programtically, please do not modify
def get_bb_floorfirst(*args, decode_return=False):
    """return = lpsolve('get_bb_floorfirst', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_bb_floorfirst', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_bb_floorfirst', *encode_args(args))


# This function was generated programtically, please do not modify
def get_bb_rule(*args, decode_return=False):
    """return = lpsolve('get_bb_rule', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_bb_rule', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_bb_rule', *encode_args(args))


# This function was generated programtically, please do not modify
def get_bounds_tighter(*args, decode_return=False):
    """return = lpsolve('get_bounds_tighter', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_bounds_tighter', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_bounds_tighter', *encode_args(args))


# This function was generated programtically, please do not modify
def get_break_at_value(*args, decode_return=False):
    """return = lpsolve('get_break_at_value', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_break_at_value', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_break_at_value', *encode_args(args))


# This function was generated programtically, please do not modify
def get_col_name(*args, decode_return=False):
    """name = lpsolve('get_col_name', lp, column)
[names] = lpsolve('get_col_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_col_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_col_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_column(*args, decode_return=False):
    """[column, return] = lpsolve('get_column', lp, col_nr)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_column', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_column', *encode_args(args))


# This function was generated programtically, please do not modify
def get_columnex(*args, decode_return=False):
    """[column, return] = lpsolve('get_columnex', lp, col_nr)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_columnex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_columnex', *encode_args(args))


# This function was generated programtically, please do not modify
def get_constr_type(*args, decode_return=False):
    """return = lpsolve('get_constr_type', lp, row)
[constr_type] = lpsolve('get_constr_type', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_constr_type', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_constr_type', *encode_args(args))


# This function was generated programtically, please do not modify
def get_constr_value(*args, decode_return=False):
    """return = lpsolve('get_constr_value', lp, row {, primsolution})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_constr_value', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_constr_value', *encode_args(args))


# This function was generated programtically, please do not modify
def get_constraints(*args, decode_return=False):
    """[constr, return] = lpsolve('get_constraints', lp)
The same information can also be obtained via lpsolve('get_constraints', lp). This shows the result on screen."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_constraints', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_constraints', *encode_args(args))


# This function was generated programtically, please do not modify
def get_dual_solution(*args, decode_return=False):
    """[duals, return] = lpsolve('get_dual_solution', lp)
The same information can be obtained via lpsolve('get_dual_solution', lp). This shows the result on screen."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_dual_solution', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_dual_solution', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epsb(*args, decode_return=False):
    """return = lpsolve('get_epsb', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epsb', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epsb', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epsd(*args, decode_return=False):
    """return = lpsolve('get_epsd', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epsd', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epsd', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epsel(*args, decode_return=False):
    """return = lpsolve('get_epsel', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epsel', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epsel', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epsint(*args, decode_return=False):
    """return = lpsolve('get_epsint', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epsint', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epsint', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epsperturb(*args, decode_return=False):
    """return = lpsolve('get_epsperturb', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epsperturb', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epsperturb', *encode_args(args))


# This function was generated programtically, please do not modify
def get_epspivot(*args, decode_return=False):
    """return = lpsolve('get_epspivot', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_epspivot', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_epspivot', *encode_args(args))


# This function was generated programtically, please do not modify
def get_improve(*args, decode_return=False):
    """return = lpsolve('get_improve', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_improve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_improve', *encode_args(args))


# This function was generated programtically, please do not modify
def get_infinite(*args, decode_return=False):
    """return = lpsolve('get_infinite', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_infinite', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_infinite', *encode_args(args))


# This function was generated programtically, please do not modify
def get_lowbo(*args, decode_return=False):
    """return = lpsolve('get_lowbo', lp, column)
[return] = lpsolve('get_lowbo', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_lowbo', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_lowbo', *encode_args(args))


# This function was generated programtically, please do not modify
def get_lp_index(*args, decode_return=False):
    """return = lpsolve('get_lp_index', lp, orig_index)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_lp_index', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_lp_index', *encode_args(args))


# This function was generated programtically, please do not modify
def get_lp_name(*args, decode_return=False):
    """name = lpsolve('get_lp_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_lp_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_lp_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_mat(*args, decode_return=False):
    """value = lpsolve('get_mat', lp, row, col)
[matrix, return] = lpsolve('get_mat', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_mat', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_mat', *encode_args(args))


# This function was generated programtically, please do not modify
def get_max_level(*args, decode_return=False):
    """return = lpsolve('get_max_level', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_max_level', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_max_level', *encode_args(args))


# This function was generated programtically, please do not modify
def get_maxpivot(*args, decode_return=False):
    """return = lpsolve('get_maxpivot', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_maxpivot', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_maxpivot', *encode_args(args))


# This function was generated programtically, please do not modify
def get_mip_gap(*args, decode_return=False):
    """return = lpsolve('get_mip_gap', lp, absolute)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_mip_gap', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_mip_gap', *encode_args(args))


# This function was generated programtically, please do not modify
def get_nameindex(*args, decode_return=False):
    """return = lpsolve('get_nameindex', lp, name, isrow)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_nameindex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_nameindex', *encode_args(args))


# This function was generated programtically, please do not modify
def get_Ncolumns(*args, decode_return=False):
    """return = lpsolve('get_Ncolumns', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_Ncolumns', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_Ncolumns', *encode_args(args))


# This function was generated programtically, please do not modify
def get_negrange(*args, decode_return=False):
    """return = lpsolve('get_negrange', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_negrange', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_negrange', *encode_args(args))


# This function was generated programtically, please do not modify
def get_nonzeros(*args, decode_return=False):
    """return = lpsolve('get_nonzeros', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_nonzeros', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_nonzeros', *encode_args(args))


# This function was generated programtically, please do not modify
def get_Norig_columns(*args, decode_return=False):
    """return = lpsolve('get_Norig_columns', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_Norig_columns', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_Norig_columns', *encode_args(args))


# This function was generated programtically, please do not modify
def get_Norig_rows(*args, decode_return=False):
    """return = lpsolve('get_Norig_rows', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_Norig_rows', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_Norig_rows', *encode_args(args))


# This function was generated programtically, please do not modify
def get_Nrows(*args, decode_return=False):
    """return = lpsolve('get_Nrows', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_Nrows', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_Nrows', *encode_args(args))


# This function was generated programtically, please do not modify
def get_obj_bound(*args, decode_return=False):
    """return = lpsolve('get_obj_bound', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_obj_bound', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_obj_bound', *encode_args(args))


# This function was generated programtically, please do not modify
def get_objective(*args, decode_return=False):
    """return = lpsolve('get_objective', lp)
The same information can be obtained via lpsolve('get_objective', lp). This shows the result on screen."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_objective', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_objective', *encode_args(args))


# This function was generated programtically, please do not modify
def get_orig_index(*args, decode_return=False):
    """return = lpsolve('get_orig_index', lp, lp_index)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_orig_index', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_orig_index', *encode_args(args))


# This function was generated programtically, please do not modify
def get_origcol_name(*args, decode_return=False):
    """name = lpsolve('get_origcol_name', lp, column)
[names] = lpsolve('get_origcol_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_origcol_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_origcol_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_origrow_name(*args, decode_return=False):
    """name = lpsolve('get_origrow_name', lp, row)
[names] = lpsolve('get_origrow_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_origrow_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_origrow_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_pivoting(*args, decode_return=False):
    """return = lpsolve('get_pivoting', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_pivoting', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_pivoting', *encode_args(args))


# This function was generated programtically, please do not modify
def get_presolve(*args, decode_return=False):
    """return = lpsolve('get_presolve', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_presolve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_presolve', *encode_args(args))


# This function was generated programtically, please do not modify
def get_presolveloops(*args, decode_return=False):
    """return = lpsolve('get_presolveloops', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_presolveloops', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_presolveloops', *encode_args(args))


# This function was generated programtically, please do not modify
def get_primal_solution(*args, decode_return=False):
    """[pv, return] = lpsolve('get_primal_solution', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_primal_solution', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_primal_solution', *encode_args(args))


# This function was generated programtically, please do not modify
def get_print_sol(*args, decode_return=False):
    """return = lpsolve('get_print_sol', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_print_sol', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_print_sol', *encode_args(args))


# This function was generated programtically, please do not modify
def get_rh(*args, decode_return=False):
    """return = lpsolve('get_rh', lp, row)
[rh] = lpsolve('get_rh', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_rh', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_rh', *encode_args(args))


# This function was generated programtically, please do not modify
def get_rh_range(*args, decode_return=False):
    """return = lpsolve('get_rh_range', lp, row)
[rh_ranges] = lpsolve('get_rh_range', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_rh_range', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_rh_range', *encode_args(args))


# This function was generated programtically, please do not modify
def get_row(*args, decode_return=False):
    """[row, return] = lpsolve('get_row', lp, row_nr)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_row', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_row', *encode_args(args))


# This function was generated programtically, please do not modify
def get_rowex(*args, decode_return=False):
    """[row, return] = lpsolve('get_rowex', lp, row_nr)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_rowex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_rowex', *encode_args(args))


# This function was generated programtically, please do not modify
def get_row_name(*args, decode_return=False):
    """name = lpsolve('get_row_name', lp, row)
[names] = lpsolve('get_row_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_row_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_row_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_scalelimit(*args, decode_return=False):
    """return = lpsolve('get_scalelimit', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_scalelimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_scalelimit', *encode_args(args))


# This function was generated programtically, please do not modify
def get_scaling(*args, decode_return=False):
    """return = lpsolve('get_scaling', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_scaling', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_scaling', *encode_args(args))


# This function was generated programtically, please do not modify
def get_sensitivity_obj(*args, decode_return=False):
    """[objfrom, objtill, objfromvalue, objtillvalue, return] = lpsolve('get_sensitivity_obj', lp)
The objfrom, objtill, objfromvalue, objtillvalue arguments in the API documentation are here the return values. Note that Python allows the return of fewer variables. For example if only objfrom and objtill are needed then the call can be [objfrom, objtill] = lpsolve('get_sensitivity_obj', lp). The unrequested values are even not calculated."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_sensitivity_obj', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_sensitivity_obj', *encode_args(args))


# This function was generated programtically, please do not modify
def get_sensitivity_objex(*args, decode_return=False):
    """[objfrom, objtill, objfromvalue, objtillvalue, return] = lpsolve('get_sensitivity_objex', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_sensitivity_objex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_sensitivity_objex', *encode_args(args))


# This function was generated programtically, please do not modify
def get_sensitivity_rhs(*args, decode_return=False):
    """[duals, dualsfrom, dualstill, return] = lpsolve('get_sensitivity_rhs', lp)
The duals, dualsfrom, dualstill arguments in the API documentation are here the return values. Note that Python allows the return of fewer variables. For example if only duals is needed then the call can be [duals] = lpsolve('get_sensitivity_rhs', lp). The unrequested values are even not calculated."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_sensitivity_rhs', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_sensitivity_rhs', *encode_args(args))


# This function was generated programtically, please do not modify
def get_sensitivity_rhsex(*args, decode_return=False):
    """[duals, dualsfrom, dualstill, return] = lpsolve('get_sensitivity_rhsex', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_sensitivity_rhsex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_sensitivity_rhsex', *encode_args(args))


# This function was generated programtically, please do not modify
def get_simplextype(*args, decode_return=False):
    """return = lpsolve('get_simplextype', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_simplextype', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_simplextype', *encode_args(args))


# This function was generated programtically, please do not modify
def get_solutioncount(*args, decode_return=False):
    """return = lpsolve('get_solutioncount', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_solutioncount', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_solutioncount', *encode_args(args))


# This function was generated programtically, please do not modify
def get_solutionlimit(*args, decode_return=False):
    """return = lpsolve('get_solutionlimit', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_solutionlimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_solutionlimit', *encode_args(args))


# This function was generated programtically, please do not modify
def get_status(*args, decode_return=False):
    """return = lpsolve('get_status', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_status', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_status', *encode_args(args))


# This function was generated programtically, please do not modify
def get_statustext(*args, decode_return=False):
    """return = lpsolve('get_statustext', lp, statuscode)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_statustext', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_statustext', *encode_args(args))


# This function was generated programtically, please do not modify
def get_timeout(*args, decode_return=False):
    """return = lpsolve('get_timeout', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_timeout', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_timeout', *encode_args(args))


# This function was generated programtically, please do not modify
def get_total_iter(*args, decode_return=False):
    """return = lpsolve('get_total_iter', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_total_iter', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_total_iter', *encode_args(args))


# This function was generated programtically, please do not modify
def get_total_nodes(*args, decode_return=False):
    """return = lpsolve('get_total_nodes', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_total_nodes', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_total_nodes', *encode_args(args))


# This function was generated programtically, please do not modify
def get_upbo(*args, decode_return=False):
    """return = lpsolve('get_upbo', lp, column)
[upbo] = lpsolve('get_upbo', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_upbo', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_upbo', *encode_args(args))


# This function was generated programtically, please do not modify
def get_var_branch(*args, decode_return=False):
    """return = lpsolve('get_var_branch', lp, column)
[var_branch] = lpsolve('get_var_branch', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_var_branch', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_var_branch', *encode_args(args))


# This function was generated programtically, please do not modify
def get_var_dualresult(*args, decode_return=False):
    """return = lpsolve('get_var_dualresult', lp, index)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_var_dualresult', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_var_dualresult', *encode_args(args))


# This function was generated programtically, please do not modify
def get_var_primalresult(*args, decode_return=False):
    """return = lpsolve('get_var_primalresult', lp, index)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_var_primalresult', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_var_primalresult', *encode_args(args))


# This function was generated programtically, please do not modify
def get_var_priority(*args, decode_return=False):
    """return = lpsolve('get_var_priority', lp, column)
[var_priority] = lpsolve('get_var_priority', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_var_priority', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_var_priority', *encode_args(args))


# This function was generated programtically, please do not modify
def get_variables(*args, decode_return=False):
    """[var, return] = lpsolve('get_variables', lp)
The same information can also be obtained via lpsolve('get_variables', lp). This shows the result on screen."""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_variables', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_variables', *encode_args(args))


# This function was generated programtically, please do not modify
def get_verbose(*args, decode_return=False):
    """return = lpsolve('get_verbose', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_verbose', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_verbose', *encode_args(args))


# This function was generated programtically, please do not modify
def get_working_objective(*args, decode_return=False):
    """return = lpsolve('get_working_objective', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_working_objective', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_working_objective', *encode_args(args))


# This function was generated programtically, please do not modify
def guess_basis(*args, decode_return=False):
    """[basisvector, return] = lpsolve('guess_basis', lp, [guessvector])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'guess_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'guess_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def has_BFP(*args, decode_return=False):
    """return = lpsolve('has_BFP', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'has_BFP', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'has_BFP', *encode_args(args))


# This function was generated programtically, please do not modify
def has_XLI(*args, decode_return=False):
    """return = lpsolve('has_XLI', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'has_XLI', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'has_XLI', *encode_args(args))


# This function was generated programtically, please do not modify
def is_add_rowmode(*args, decode_return=False):
    """return = lpsolve('is_add_rowmode', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_add_rowmode', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_add_rowmode', *encode_args(args))


# This function was generated programtically, please do not modify
def is_anti_degen(*args, decode_return=False):
    """return = lpsolve('is_anti_degen', lp, testmask)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_anti_degen', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_anti_degen', *encode_args(args))


# This function was generated programtically, please do not modify
def is_binary(*args, decode_return=False):
    """return = lpsolve('is_binary', lp, column)
[binary] = lpsolve('is_binary', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_binary', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_binary', *encode_args(args))


# This function was generated programtically, please do not modify
def is_break_at_first(*args, decode_return=False):
    """return = lpsolve('is_break_at_first', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_break_at_first', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_break_at_first', *encode_args(args))


# This function was generated programtically, please do not modify
def is_constr_type(*args, decode_return=False):
    """return = lpsolve('is_constr_type', lp, row, mask)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_constr_type', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_constr_type', *encode_args(args))


# This function was generated programtically, please do not modify
def is_debug(*args, decode_return=False):
    """return = lpsolve('is_debug', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_debug', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_debug', *encode_args(args))


# This function was generated programtically, please do not modify
def is_feasible(*args, decode_return=False):
    """return = lpsolve('is_feasible', lp, [values] {, threshold})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_feasible', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_feasible', *encode_args(args))


# This function was generated programtically, please do not modify
def is_free(*args, decode_return=False):
    """return = lpsolve('is_free', lp, column)
[free] = lpsolve('is_free', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_free', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_free', *encode_args(args))


# This function was generated programtically, please do not modify
def is_unbounded(*args, decode_return=False):
    """return = lpsolve('is_unbounded', lp, column)
[free] = lpsolve('is_unbounded', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_unbounded', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_unbounded', *encode_args(args))


# This function was generated programtically, please do not modify
def is_infinite(*args, decode_return=False):
    """return = lpsolve('is_infinite', lp, value)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_infinite', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_infinite', *encode_args(args))


# This function was generated programtically, please do not modify
def is_int(*args, decode_return=False):
    """return = lpsolve('is_int', lp, column)
[int] = lpsolve('is_int', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_int', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_int', *encode_args(args))


# This function was generated programtically, please do not modify
def is_integerscaling(*args, decode_return=False):
    """return = lpsolve('is_integerscaling', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_integerscaling', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_integerscaling', *encode_args(args))


# This function was generated programtically, please do not modify
def is_maxim(*args, decode_return=False):
    """return = lpsolve('is_maxim', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_maxim', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_maxim', *encode_args(args))


# This function was generated programtically, please do not modify
def is_nativeBFP(*args, decode_return=False):
    """return = lpsolve('is_nativeBFP', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_nativeBFP', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_nativeBFP', *encode_args(args))


# This function was generated programtically, please do not modify
def is_nativeXLI(*args, decode_return=False):
    """return = lpsolve('is_nativeXLI', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_nativeXLI', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_nativeXLI', *encode_args(args))


# This function was generated programtically, please do not modify
def is_negative(*args, decode_return=False):
    """return = lpsolve('is_negative', lp, column)
[negative] = lpsolve('is_negative', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_negative', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_negative', *encode_args(args))


# This function was generated programtically, please do not modify
def is_piv_mode(*args, decode_return=False):
    """return = lpsolve('is_piv_mode', lp, testmask)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_piv_mode', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_piv_mode', *encode_args(args))


# This function was generated programtically, please do not modify
def is_piv_rule(*args, decode_return=False):
    """return = lpsolve('is_piv_rule', lp, rule)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_piv_rule', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_piv_rule', *encode_args(args))


# This function was generated programtically, please do not modify
def is_presolve(*args, decode_return=False):
    """return = lpsolve('is_presolve', lp, testmask)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_presolve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_presolve', *encode_args(args))


# This function was generated programtically, please do not modify
def is_scalemode(*args, decode_return=False):
    """return = lpsolve('is_scalemode', lp, testmask)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_scalemode', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_scalemode', *encode_args(args))


# This function was generated programtically, please do not modify
def is_scaletype(*args, decode_return=False):
    """return = lpsolve('is_scaletype', lp, scaletype)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_scaletype', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_scaletype', *encode_args(args))


# This function was generated programtically, please do not modify
def is_semicont(*args, decode_return=False):
    """return = lpsolve('is_semicont', lp, column)
[semicont] = lpsolve('is_semicont', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_semicont', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_semicont', *encode_args(args))


# This function was generated programtically, please do not modify
def is_SOS_var(*args, decode_return=False):
    """return = lpsolve('is_SOS_var', lp, column)
[SOS_var] = lpsolve('is_SOS_var', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_SOS_var', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_SOS_var', *encode_args(args))


# This function was generated programtically, please do not modify
def is_trace(*args, decode_return=False):
    """return = lpsolve('is_trace', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_trace', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_trace', *encode_args(args))


# This function was generated programtically, please do not modify
def is_use_names(*args, decode_return=False):
    """return = lpsolve('is_use_names', lp, isrow)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'is_use_names', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'is_use_names', *encode_args(args))


# This function was generated programtically, please do not modify
def lp_solve_version(*args, decode_return=False):
    """versionstring = lpsolve('lp_solve_version')"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'lp_solve_version', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'lp_solve_version', *encode_args(args))


# This function was generated programtically, please do not modify
def make_lp(*args, decode_return=False):
    """lp_handle = lpsolve('make_lp', rows, columns)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'make_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'make_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def print_constraints(*args, decode_return=False):
    """lpsolve('print_constraints', lp {, columns})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_constraints', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_constraints', *encode_args(args))


# This function was generated programtically, please do not modify
def print_debugdump(*args, decode_return=False):
    """return = lpsolve('print_debugdump', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_debugdump', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_debugdump', *encode_args(args))


# This function was generated programtically, please do not modify
def print_duals(*args, decode_return=False):
    """lpsolve('print_duals', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_duals', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_duals', *encode_args(args))


# This function was generated programtically, please do not modify
def print_lp(*args, decode_return=False):
    """lpsolve('print_lp', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def print_objective(*args, decode_return=False):
    """lpsolve('print_objective', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_objective', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_objective', *encode_args(args))


# This function was generated programtically, please do not modify
def print_scales(*args, decode_return=False):
    """lpsolve('print_scales', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_scales', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_scales', *encode_args(args))


# This function was generated programtically, please do not modify
def print_solution(*args, decode_return=False):
    """lpsolve('print_solution', lp {, columns})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_solution', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_solution', *encode_args(args))


# This function was generated programtically, please do not modify
def print_str(*args, decode_return=False):
    """lpsolve('print_str', lp, str)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_str', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_str', *encode_args(args))


# This function was generated programtically, please do not modify
def print_tableau(*args, decode_return=False):
    """lpsolve('print_tableau', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_tableau', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_tableau', *encode_args(args))


# This function was generated programtically, please do not modify
def read_basis(*args, decode_return=False):
    """[ret, info] = lpsolve('read_basis', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def read_freemps(*args, decode_return=False):
    """lp_handle = lpsolve('read_freemps', filename {, options})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_freemps', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_freemps', *encode_args(args))


# This function was generated programtically, please do not modify
def read_freeMPS(*args, decode_return=False):
    """lp_handle = lpsolve('read_freeMPS', filename {, options})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_freeMPS', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_freeMPS', *encode_args(args))


# This function was generated programtically, please do not modify
def read_lp(*args, decode_return=False):
    """lp_handle = lpsolve('read_lp', filename {, verbose {, lp_name}})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def read_LP(*args, decode_return=False):
    """lp_handle = lpsolve('read_LP', filename {, verbose {, lp_name}})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_LP', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_LP', *encode_args(args))


# This function was generated programtically, please do not modify
def read_mps(*args, decode_return=False):
    """lp_handle = lpsolve('read_mps', filename {, options})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_mps', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_mps', *encode_args(args))


# This function was generated programtically, please do not modify
def read_MPS(*args, decode_return=False):
    """lp_handle = lpsolve('read_MPS', filename {, options})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_MPS', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_MPS', *encode_args(args))


# This function was generated programtically, please do not modify
def read_params(*args, decode_return=False):
    """return = lpsolve('read_params', lp, filename {, options })"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_params', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_params', *encode_args(args))


# This function was generated programtically, please do not modify
def set_basisvar(*args, decode_return=False):
    """lpsolve('set_basisvar', lp, basisPos, enteringCol)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_basisvar', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_basisvar', *encode_args(args))


# This function was generated programtically, please do not modify
def set_add_rowmode(*args, decode_return=False):
    """return = lpsolve('set_add_rowmode', lp, turnon)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_add_rowmode', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_add_rowmode', *encode_args(args))


# This function was generated programtically, please do not modify
def set_anti_degen(*args, decode_return=False):
    """lpsolve('set_anti_degen', lp, anti_degen)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_anti_degen', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_anti_degen', *encode_args(args))


# This function was generated programtically, please do not modify
def set_basis(*args, decode_return=False):
    """return = lpsolve('set_basis', lp, [bascolumn], nonbasic)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def set_basiscrash(*args, decode_return=False):
    """lpsolve('set_basiscrash', lp, mode)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_basiscrash', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_basiscrash', *encode_args(args))


# This function was generated programtically, please do not modify
def set_bb_depthlimit(*args, decode_return=False):
    """lpsolve('set_bb_depthlimit', lp, bb_maxlevel)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_bb_depthlimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_bb_depthlimit', *encode_args(args))


# This function was generated programtically, please do not modify
def set_bb_floorfirst(*args, decode_return=False):
    """lpsolve('set_bb_floorfirst', lp, bb_floorfirst)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_bb_floorfirst', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_bb_floorfirst', *encode_args(args))


# This function was generated programtically, please do not modify
def set_bb_rule(*args, decode_return=False):
    """lpsolve('set_bb_rule', lp, bb_rule)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_bb_rule', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_bb_rule', *encode_args(args))


# This function was generated programtically, please do not modify
def set_BFP(*args, decode_return=False):
    """return = lpsolve('set_BFP', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_BFP', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_BFP', *encode_args(args))


# This function was generated programtically, please do not modify
def set_binary(*args, decode_return=False):
    """return = lpsolve('set_binary', lp, column, must_be_bin)
return = lpsolve('set_binary', lp, [must_be_bin])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_binary', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_binary', *encode_args(args))


# This function was generated programtically, please do not modify
def set_bounds(*args, decode_return=False):
    """return = lpsolve('set_bounds', lp, column, lower, upper)
return = lpsolve('set_bounds', lp, [lower], [upper])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_bounds', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_bounds', *encode_args(args))


# This function was generated programtically, please do not modify
def set_bounds_tighter(*args, decode_return=False):
    """lpsolve('set_bounds_tighter', lp, tighten)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_bounds_tighter', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_bounds_tighter', *encode_args(args))


# This function was generated programtically, please do not modify
def set_break_at_first(*args, decode_return=False):
    """lpsolve('set_break_at_first', lp, break_at_first)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_break_at_first', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_break_at_first', *encode_args(args))


# This function was generated programtically, please do not modify
def set_break_at_value(*args, decode_return=False):
    """lpsolve('set_break_at_value', lp, break_at_value)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_break_at_value', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_break_at_value', *encode_args(args))


# This function was generated programtically, please do not modify
def set_col_name(*args, decode_return=False):
    """return = lpsolve('set_col_name', lp, column, name)
return = lpsolve('set_col_name', lp, [names])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_col_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_col_name', *encode_args(args))


# This function was generated programtically, please do not modify
def set_column(*args, decode_return=False):
    """return = lpsolve('set_column', lp, col_no, [column])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_column', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_column', *encode_args(args))


# This function was generated programtically, please do not modify
def set_columnex(*args, decode_return=False):
    """return = lpsolve('set_columnex', lp, col_no, [column])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_columnex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_columnex', *encode_args(args))


# This function was generated programtically, please do not modify
def set_constr_type(*args, decode_return=False):
    """return = lpsolve('set_constr_type', lp, row, con_type)
return = lpsolve('set_constr_type', lp, [con_type])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_constr_type', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_constr_type', *encode_args(args))


# This function was generated programtically, please do not modify
def set_debug(*args, decode_return=False):
    """lpsolve('set_debug', lp, debug)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_debug', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_debug', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epsb(*args, decode_return=False):
    """lpsolve('set_epsb', lp, epsb)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epsb', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epsb', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epsd(*args, decode_return=False):
    """lpsolve('set_epsd', lp, epsd)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epsd', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epsd', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epsel(*args, decode_return=False):
    """lpsolve('set_epsel', lp, epsel)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epsel', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epsel', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epsint(*args, decode_return=False):
    """lpsolve('set_epsint', lp, epsint)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epsint', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epsint', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epslevel(*args, decode_return=False):
    """lpsolve('set_epslevel', lp, epslevel)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epslevel', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epslevel', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epsperturb(*args, decode_return=False):
    """lpsolve('set_epsperturb', lp, epsperturb)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epsperturb', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epsperturb', *encode_args(args))


# This function was generated programtically, please do not modify
def set_epspivot(*args, decode_return=False):
    """lpsolve('set_epspivot', lp, epspivot)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_epspivot', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_epspivot', *encode_args(args))


# This function was generated programtically, please do not modify
def set_free(*args, decode_return=False):
    """return = lpsolve('set_free', lp, column)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_free', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_free', *encode_args(args))


# This function was generated programtically, please do not modify
def set_unbounded(*args, decode_return=False):
    """return = lpsolve('set_unbounded', lp, column)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_unbounded', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_unbounded', *encode_args(args))


# This function was generated programtically, please do not modify
def set_improve(*args, decode_return=False):
    """lpsolve('set_improve', lp, improve)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_improve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_improve', *encode_args(args))


# This function was generated programtically, please do not modify
def set_infinite(*args, decode_return=False):
    """lpsolve('set_infinite', lp, infinite)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_infinite', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_infinite', *encode_args(args))


# This function was generated programtically, please do not modify
def set_int(*args, decode_return=False):
    """return = lpsolve('set_int', lp, column, must_be_int)
return = lpsolve('set_int', lp, [must_be_int])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_int', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_int', *encode_args(args))


# This function was generated programtically, please do not modify
def set_lowbo(*args, decode_return=False):
    """return = lpsolve('set_lowbo', lp, column, value)
return = lpsolve('set_lowbo', lp, [values])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_lowbo', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_lowbo', *encode_args(args))


# This function was generated programtically, please do not modify
def set_lp_name(*args, decode_return=False):
    """return = lpsolve('set_lp_name', lp, name)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_lp_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_lp_name', *encode_args(args))


# This function was generated programtically, please do not modify
def set_mat(*args, decode_return=False):
    """return = lpsolve('set_mat', lp, row, column, value)
return = lpsolve('set_mat', lp, [matrix])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_mat', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_mat', *encode_args(args))


# This function was generated programtically, please do not modify
def set_maxim(*args, decode_return=False):
    """lpsolve('set_maxim', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_maxim', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_maxim', *encode_args(args))


# This function was generated programtically, please do not modify
def set_maxpivot(*args, decode_return=False):
    """lpsolve('set_maxpivot', max_num_inv)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_maxpivot', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_maxpivot', *encode_args(args))


# This function was generated programtically, please do not modify
def set_minim(*args, decode_return=False):
    """lpsolve('set_minim', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_minim', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_minim', *encode_args(args))


# This function was generated programtically, please do not modify
def set_mip_gap(*args, decode_return=False):
    """lpsolve('set_mip_gap', lp, absolute, mip_gap)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_mip_gap', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_mip_gap', *encode_args(args))


# This function was generated programtically, please do not modify
def set_negrange(*args, decode_return=False):
    """lpsolve('set_negrange', negrange)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_negrange', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_negrange', *encode_args(args))


# This function was generated programtically, please do not modify
def set_obj(*args, decode_return=False):
    """return = lpsolve('set_obj', lp, column, value)
return = lpsolve('set_obj', lp, [values])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_obj', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_obj', *encode_args(args))


# This function was generated programtically, please do not modify
def set_obj_bound(*args, decode_return=False):
    """lpsolve('set_obj_bound', lp, obj_bound)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_obj_bound', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_obj_bound', *encode_args(args))


# This function was generated programtically, please do not modify
def set_obj_fn(*args, decode_return=False):
    """return = lpsolve('set_obj_fn', lp, [row])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_obj_fn', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_obj_fn', *encode_args(args))


# This function was generated programtically, please do not modify
def set_obj_fnex(*args, decode_return=False):
    """return = lpsolve('set_obj_fnex', lp, [row])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_obj_fnex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_obj_fnex', *encode_args(args))


# This function was generated programtically, please do not modify
def set_outputfile(*args, decode_return=False):
    """return = lpsolve('set_outputfile', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_outputfile', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_outputfile', *encode_args(args))


# This function was generated programtically, please do not modify
def set_pivoting(*args, decode_return=False):
    """lpsolve('set_pivoting', lp, pivoting)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_pivoting', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_pivoting', *encode_args(args))


# This function was generated programtically, please do not modify
def set_preferdual(*args, decode_return=False):
    """lpsolve('set_preferdual', lp, dodual)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_preferdual', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_preferdual', *encode_args(args))


# This function was generated programtically, please do not modify
def set_presolve(*args, decode_return=False):
    """lpsolve('set_presolve', lp, do_presolve {, maxloops})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_presolve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_presolve', *encode_args(args))


# This function was generated programtically, please do not modify
def set_print_sol(*args, decode_return=False):
    """lpsolve('set_print_sol', lp, print_sol)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_print_sol', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_print_sol', *encode_args(args))


# This function was generated programtically, please do not modify
def set_rh(*args, decode_return=False):
    """return = lpsolve('set_rh', lp, row, value)
return = lpsolve('set_rh', lp, [values])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_rh', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_rh', *encode_args(args))


# This function was generated programtically, please do not modify
def set_rh_range(*args, decode_return=False):
    """return = lpsolve('set_rh_range', lp, row, deltavalue)
return = lpsolve('set_rh_range', lp, [deltavalues])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_rh_range', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_rh_range', *encode_args(args))


# This function was generated programtically, please do not modify
def set_rh_vec(*args, decode_return=False):
    """lpsolve('set_rh_vec', lp, [rh])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_rh_vec', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_rh_vec', *encode_args(args))


# This function was generated programtically, please do not modify
def set_row(*args, decode_return=False):
    """return = lpsolve('set_row', lp, row_no, [row])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_row', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_row', *encode_args(args))


# This function was generated programtically, please do not modify
def set_rowex(*args, decode_return=False):
    """return = lpsolve('set_rowex', lp, row_no, [row])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_rowex', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_rowex', *encode_args(args))


# This function was generated programtically, please do not modify
def set_row_name(*args, decode_return=False):
    """return = lpsolve('set_row_name', lp, row, name)
return = lpsolve('set_row_name', lp, [names])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_row_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_row_name', *encode_args(args))


# This function was generated programtically, please do not modify
def set_scalelimit(*args, decode_return=False):
    """lpsolve('set_scalelimit', lp, scalelimit)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_scalelimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_scalelimit', *encode_args(args))


# This function was generated programtically, please do not modify
def set_scaling(*args, decode_return=False):
    """lpsolve('set_scaling', lp, scalemode)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_scaling', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_scaling', *encode_args(args))


# This function was generated programtically, please do not modify
def set_semicont(*args, decode_return=False):
    """return = lpsolve('set_semicont', lp, column, must_be_sc)
return = lpsolve('set_semicont', lp, [must_be_sc])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_semicont', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_semicont', *encode_args(args))


# This function was generated programtically, please do not modify
def set_sense(*args, decode_return=False):
    """lpsolve('set_sense', lp, maximize)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_sense', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_sense', *encode_args(args))


# This function was generated programtically, please do not modify
def set_simplextype(*args, decode_return=False):
    """lpsolve('set_simplextype', lp, simplextype)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_simplextype', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_simplextype', *encode_args(args))


# This function was generated programtically, please do not modify
def set_solutionlimit(*args, decode_return=False):
    """lpsolve('set_solutionlimit', lp, simplextype)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_solutionlimit', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_solutionlimit', *encode_args(args))


# This function was generated programtically, please do not modify
def set_timeout(*args, decode_return=False):
    """lpsolve('set_timeout', lp, sectimeout)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_timeout', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_timeout', *encode_args(args))


# This function was generated programtically, please do not modify
def set_trace(*args, decode_return=False):
    """lpsolve('set_trace', lp, trace)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_trace', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_trace', *encode_args(args))


# This function was generated programtically, please do not modify
def set_upbo(*args, decode_return=False):
    """return = lpsolve('set_upbo', lp, column, value)
return = lpsolve('set_upbo', lp, [values])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_upbo', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_upbo', *encode_args(args))


# This function was generated programtically, please do not modify
def set_use_names(*args, decode_return=False):
    """lpsolve('set_use_names', lp, isrow, use_names)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_use_names', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_use_names', *encode_args(args))


# This function was generated programtically, please do not modify
def set_var_branch(*args, decode_return=False):
    """return = lpsolve('set_var_branch', lp, column, branch_mode)
return = lpsolve('set_var_branch', lp, [branch_mode])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_var_branch', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_var_branch', *encode_args(args))


# This function was generated programtically, please do not modify
def set_var_weights(*args, decode_return=False):
    """return = lpsolve('set_var_weights', lp, [weights])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_var_weights', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_var_weights', *encode_args(args))


# This function was generated programtically, please do not modify
def set_verbose(*args, decode_return=False):
    """lpsolve('set_verbose', lp, verbose)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_verbose', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_verbose', *encode_args(args))


# This function was generated programtically, please do not modify
def set_XLI(*args, decode_return=False):
    """return = lpsolve('set_XLI', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'set_XLI', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'set_XLI', *encode_args(args))


# This function was generated programtically, please do not modify
def solve(*args, decode_return=False):
    """result = lpsolve('solve', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'solve', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'solve', *encode_args(args))


# This function was generated programtically, please do not modify
def time_elapsed(*args, decode_return=False):
    """return = lpsolve('time_elapsed', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'time_elapsed', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'time_elapsed', *encode_args(args))


# This function was generated programtically, please do not modify
def unscale(*args, decode_return=False):
    """lpsolve('unscale', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'unscale', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'unscale', *encode_args(args))


# This function was generated programtically, please do not modify
def write_basis(*args, decode_return=False):
    """lpsolve('write_basis', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_basis', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_basis', *encode_args(args))


# This function was generated programtically, please do not modify
def write_freemps(*args, decode_return=False):
    """return = lpsolve('write_freemps', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_freemps', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_freemps', *encode_args(args))


# This function was generated programtically, please do not modify
def write_freeMPS(*args, decode_return=False):
    """return = lpsolve('write_freeMPS', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_freeMPS', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_freeMPS', *encode_args(args))


# This function was generated programtically, please do not modify
def write_lp(*args, decode_return=False):
    """return = lpsolve('write_lp', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_lp', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_lp', *encode_args(args))


# This function was generated programtically, please do not modify
def write_LP(*args, decode_return=False):
    """return = lpsolve('write_LP', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_LP', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_LP', *encode_args(args))


# This function was generated programtically, please do not modify
def write_mps(*args, decode_return=False):
    """return = lpsolve('write_mps', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_mps', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_mps', *encode_args(args))


# This function was generated programtically, please do not modify
def write_MPS(*args, decode_return=False):
    """return = lpsolve('write_MPS', lp, filename)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_MPS', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_MPS', *encode_args(args))


# This function was generated programtically, please do not modify
def write_XLI(*args, decode_return=False):
    """return = lpsolve('write_XLI', lp, filename {, options {, results}})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'write_XLI', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'write_XLI', *encode_args(args))


# This function was generated programtically, please do not modify
def get_col_names(*args, decode_return=False):
    """[names] = lpsolve('get_col_names', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_col_names', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_col_names', *encode_args(args))


# This function was generated programtically, please do not modify
def get_constr_types(*args, decode_return=False):
    """[constr_type] = lpsolve('get_constr_types', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_constr_types', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_constr_types', *encode_args(args))


# This function was generated programtically, please do not modify
def get_int(*args, decode_return=False):
    """[int] = lpsolve('get_int', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_int', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_int', *encode_args(args))


# This function was generated programtically, please do not modify
def get_no_cols(*args, decode_return=False):
    """return = lpsolve('get_no_cols', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_no_cols', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_no_cols', *encode_args(args))


# This function was generated programtically, please do not modify
def get_no_rows(*args, decode_return=False):
    """return = lpsolve('get_no_rows', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_no_rows', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_no_rows', *encode_args(args))


# This function was generated programtically, please do not modify
def get_objective_name(*args, decode_return=False):
    """name = lpsolve('get_objective_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_objective_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_objective_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_obj_fn(*args, decode_return=False):
    """[row_vec, return] = lpsolve('get_obj_fn', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_obj_fn', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_obj_fn', *encode_args(args))


# This function was generated programtically, please do not modify
def get_obj_fun(*args, decode_return=False):
    """[row_vec, return] = lpsolve('get_obj_fun', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_obj_fun', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_obj_fun', *encode_args(args))


# This function was generated programtically, please do not modify
def get_problem_name(*args, decode_return=False):
    """name = lpsolve('get_problem_name', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_problem_name', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_problem_name', *encode_args(args))


# This function was generated programtically, please do not modify
def get_reduced_costs(*args, decode_return=False):
    """[costs] = lpsolve('get_reduced_costs', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_reduced_costs', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_reduced_costs', *encode_args(args))


# This function was generated programtically, please do not modify
def get_row_names(*args, decode_return=False):
    """[names] = lpsolve('get_row_names', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_row_names', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_row_names', *encode_args(args))


# This function was generated programtically, please do not modify
def get_solution(*args, decode_return=False):
    """[obj, x, duals, return] = lpsolve('get_solution', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_solution', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_solution', *encode_args(args))


# This function was generated programtically, please do not modify
def mat_elm(*args, decode_return=False):
    """value = lpsolve('mat_elm', lp)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'mat_elm', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'mat_elm', *encode_args(args))


# This function was generated programtically, please do not modify
def print_handle(*args, decode_return=False):
    """[handle_vec] = lpsolve('print_handle')"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'print_handle', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'print_handle', *encode_args(args))


# This function was generated programtically, please do not modify
def read_lp_file(*args, decode_return=False):
    """lp_handle = lpsolve('read_lp_file', filename {, verbose {, lp_name}})"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'read_lp_file', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'read_lp_file', *encode_args(args))


# This function was generated programtically, please do not modify
def get_handle(*args, decode_return=False):
    """lp_handle = lpsolve('get_handle', lp_name)"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'get_handle', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'get_handle', *encode_args(args))


# This function was generated programtically, please do not modify
def return_constants(*args, decode_return=False):
    """return_constants = lpsolve('return_constants'[, return_constants])"""
    if decode_return:
        return decode_args(lpsolve55.lpsolve(b'return_constants', *encode_args(args)))
    else:
        return lpsolve55.lpsolve(b'return_constants', *encode_args(args))


# END FUNCTIONS

def decode_args(args):
    rtn = []
    for arg in args:
        if (type(arg) == str):
            rtn.append(arg.decode('utf-8'))
        elif (type(arg) == list):
            rtn.append(decode_args(arg))
        else:
            rtn.append(arg)
    if type(args) == tuple:
        return tuple(rtn)
    else: # otherwise assume it is list
        return rtn

def encode_args(args):
    rtn = []
    for arg in args:
        if (type(arg) == str):
            rtn.append(arg.encode('utf-8'))
        elif (type(arg) == list):
            rtn.append(encode_args(arg))
        else:
            rtn.append(arg)
    if type(args) == tuple:
        return tuple(rtn)
    else: # otherwise assume it is list
        return rtn

# check whether a string is ASCII, used internally
def __is_ascii(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True
