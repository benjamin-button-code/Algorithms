func quickSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }

    let pivot = array[Int.random(in: 0...array.count-1)]
    // sub-array of all the elements less than the pivot
    let less = array.filter {$0 < pivot}
    // sub-array of all the elements equal to the pivot
    let equal = array.filter {$0 == pivot}
    // sub-array of all the elements greater than the pivot
    let greater = array.filter {$0 > pivot}
    return quickSort(less) + equal + quickSort(greater)
}
