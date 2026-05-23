//! Rust twin of the Python `funclib` module.
//!
//! Hand-curated from `depyler transpile funclib/funcmod.py` and held to
//! the same contracts: every public function asserts its postcondition
//! and is exercised by `proptest`-based property tests.

/// Canonical ordered list of adult Brazilian Jiu-Jitsu belts.
pub const BJJ_BELTS: [&str; 5] = ["white", "blue", "purple", "brown", "black"];

/// Return the ordered list of adult belts in Brazilian Jiu-Jitsu.
///
/// # Contract
/// - Ensures: returns exactly the five canonical adult belts, in rank order.
pub fn list_of_belts_in_bjj() -> Vec<String> {
    let belts: Vec<String> = BJJ_BELTS.iter().map(|s| (*s).to_string()).collect();
    debug_assert_eq!(belts.len(), 5);
    belts
}

/// Count the BJJ belts.
///
/// # Contract
/// - Ensures: result equals the number of canonical BJJ belts (5).
pub fn count_belts() -> usize {
    let n = list_of_belts_in_bjj().len();
    debug_assert_eq!(n, 5);
    n
}

#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    #[test]
    fn list_of_belts_in_bjj_matches_canonical_order() {
        assert_eq!(
            list_of_belts_in_bjj(),
            vec!["white", "blue", "purple", "brown", "black"]
        );
    }

    #[test]
    fn count_belts_is_five() {
        assert_eq!(count_belts(), 5);
    }

    #[test]
    fn belts_are_rank_ordered() {
        assert_eq!(BJJ_BELTS[0], "white");
        assert_eq!(BJJ_BELTS[BJJ_BELTS.len() - 1], "black");
    }

    proptest! {
        #[test]
        fn list_is_pure(n in 0u32..50) {
            let first = list_of_belts_in_bjj();
            for _ in 0..n {
                prop_assert_eq!(list_of_belts_in_bjj(), first.clone());
            }
        }

        #[test]
        fn count_is_invariant(n in 1u32..50) {
            for _ in 0..n {
                prop_assert_eq!(count_belts(), BJJ_BELTS.len());
            }
        }

        #[test]
        fn returned_list_is_a_copy(extra in "[a-z]{1,8}") {
            let mut first = list_of_belts_in_bjj();
            first.push(extra);
            prop_assert_eq!(list_of_belts_in_bjj().len(), BJJ_BELTS.len());
        }
    }
}
