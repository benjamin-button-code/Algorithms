func binarySearch(sortedCollection: [Int], item: Int) -> Int? {
    var low: Int = 0
    var high: Int = sortedCollection.count - 1
    var mid: Int
    var currentElement: Int

    while low <= high {
        mid = (low + high) / 2
        currentElement = sortedCollection[mid]

        if currentElement == item {
            return mid
        } else if currentElement > item {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return nil
}
