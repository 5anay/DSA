//Student 05 working solution - binary search

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int mid = nums.size() / 2;
        size_t sz = nums.size() - 1;

        if(nums[mid] == target){
            return mid;
        }

        //check if the middle of the array is larger or
        //smaller, continue the search in that array 
        
        while(mid > -1 && mid < sz){
            if(target > nums[mid]){
                //search in the upper array
                //find the 'middle'

                
                if(nums[mid] == target){
                    return mid;
                }else{
                    mid = mid + ((sz - mid) / 2);
                }

                /*while(mid != sz){
                    if(nums[mid] == target){
                        return mid;
                    }else{
                        mid++;
                    }
                }*/

            }else if(target < nums[mid]){
                //search in lower array
                //find the 'middle'
                if(nums[mid] == target){
                    return mid;
                }else{
                    mid = (mid) / 2;
                }
                /*while(mid != sz){
                    if(nums[mid] == target){
                        return mid;
                    }else{
                        mid--;
                    }

                }*/
            }

            mid++;
        }


        return -1;
        /*int count_len(int mid_position, vector<int>& nums){
            //count the length from the middle of the array to the end
        };
        for(int i = mid; i < sz; i = mid){

            mid = mid + //size of the remaining array 
        }*/
    }
};
