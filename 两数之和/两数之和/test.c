#include<stdio.h>
//�������� �ǿ� ��������ʾ�����Ǹ�������������ÿλ���ֶ��ǰ��� ���� �ķ�ʽ�洢�ģ�����ÿ���ڵ�ֻ�ܴ洢 һλ ���֡�
//
//���㽫��������ӣ�������ͬ��ʽ����һ����ʾ�͵�����
//
//����Լ���������� 0 ֮�⣬���������������� 0 ��ͷ��
struct ListNode {
      int val;
      struct ListNode *next;
};


#include<stdio.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    //ͷ�ڵ㣬��������
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* l3 = head;
    int k = 0;
    while (l1 || l2)
    {

        l3->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        l3 = l3->next;
        l3->val = ((l1 ? l1->val : 0) + (l2 ? l2->val : 0) + k) % 10;
        k = ((l1 ? l1->val : 0) + (l2 ? l2->val : 0) + k) / 10;
        if (l1)
            l1 = l1->next;
        if (l2)
            l2 = l2->next;
    }
    if (k > 0) {
        l3->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        l3 = l3->next;
        l3->val = k;
    }
    l3->next = NULL;
    return head->next;
}
int main()
{

	return 0;
}