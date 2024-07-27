/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var nodesBetweenCriticalPoints = function(head) {
    if (!head || !head.next || !head.next.next) return [-1, -1];
    
    let criticalPoints = [];
    let index = 1; // Start from the second node
    let prev = head;
    let curr = head.next;
    let next = head.next.next;
    
    while (next) {
        if ((curr.val > prev.val && curr.val > next.val) || (curr.val < prev.val && curr.val < next.val)) {
            criticalPoints.push(index);
        }
        prev = curr;
        curr = next;
        next = next.next;
        index++;
    }
    
    if (criticalPoints.length < 2) return [-1, -1];
    
    let minDist = Infinity;
    let maxDist = criticalPoints[criticalPoints.length - 1] - criticalPoints[0];
    
    for (let i = 1; i < criticalPoints.length; i++) {
        minDist = Math.min(minDist, criticalPoints[i] - criticalPoints[i - 1]);
    }
    
    return [minDist, maxDist];
};
