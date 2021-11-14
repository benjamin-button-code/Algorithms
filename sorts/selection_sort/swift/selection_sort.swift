func selectionSort<T: Comparable>(collection: [T]) -> [T] {
    let length = collection.count
    var least: Int
    var resultCollection: [T] = collection

    for i in 0..<length - 1 {
        least = i
        for j in i + 1..<length {
            if resultCollection[j] < resultCollection[least] {
                least = j
            }
        }
        if least != i {
            let temp = resultCollection[i]
            resultCollection[i] = resultCollection[least]
            resultCollection[least] = temp
        }
    }
    return resultCollection
}
